"""Pre-publish QA for a chemistry chapter artifact -- scripts the checklist in
chem/SKILL.md section 10 so it doesn't have to be re-read into a model's
context by eye on every one of the 6 chapter artifacts.

Usage:
    python3 chem/qa.py chem/build/ch4.html
    python3 chem/qa.py chem/build/ch4.html --stage lecture   # only the checks
                                                              # that apply before
                                                              # the PYQ section
                                                              # has been added
Exit code is 0 iff every applicable check passes. Chapter number and (for the
--stage default, "final") whether the PYQ section is expected are taken from
the filename ch<N>.html and chem/maps.json/chem/published.json.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CHEM_DIR = Path(__file__).resolve().parent
FIRST_CONTACT_CHAPTERS = {"4", "5", "6"}
KATEX_SCRIPTS_IN_ORDER = [
    "katex.min.js",
    "contrib/mhchem.min.js",
    "contrib/auto-render.min.js",
]


def _load_json(name: str) -> dict:
    return json.loads((CHEM_DIR / name).read_text(encoding="utf-8"))


def _chapter_number_from_filename(path: Path) -> str:
    m = re.match(r"ch(\d+)\.html?$", path.name)
    if not m:
        raise SystemExit(f"expected a filename like ch4.html, got {path.name!r}")
    return m.group(1)


def _root_token_block(html: str) -> str:
    """The bare `:root { ... }` block -- i.e. NOT inside a @media or
    :root[data-theme=...] selector. Used to check every var(--x) used
    elsewhere is actually defined in the light-mode base block."""
    m = re.search(r"(?<![\w\-\[\]\"'=(:.])\:root\s*\{([^}]*)\}", html)
    return m.group(1) if m else ""


def _strip_html_comments(html: str) -> str:
    """template.html's own authoring comments mention '<html>', '<head>' etc.
    by name as things NOT to add -- checking the raw file text would flag
    those as false positives. Strip comments first so the structural checks
    only see real markup."""
    return re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)


def run_checks(html: str, chapter_num: str, expect_pyq: bool) -> list[tuple[str, bool, str]]:
    """Returns a list of (check_name, passed, detail) tuples."""
    checks: list[tuple[str, bool, str]] = []
    stripped = _strip_html_comments(html)

    def check(name: str, passed: bool, detail: str = "") -> None:
        checks.append((name, passed, detail))

    check(
        "no doctype/html/head/body wrapper",
        not re.search(r"<!doctype|<html[ >]|<head[ >]|<body[ >]", stripped, re.IGNORECASE),
    )

    top_level_open = re.findall(r"<details\b[^>]*\bopen\b", stripped, re.IGNORECASE)
    check("no top-level <details open>", len(top_level_open) == 0, f"{len(top_level_open)} found")

    root_block = _root_token_block(stripped)
    defined_tokens = set(re.findall(r"--([\w-]+)\s*:", root_block))
    used_tokens = set(re.findall(r"var\(--([\w-]+)\)", stripped))
    undefined = sorted(t for t in used_tokens if t not in defined_tokens)
    check(
        "every var(--token) defined in bare :root",
        len(undefined) == 0,
        f"undefined: {undefined}" if undefined else "",
    )

    has_media_dark = bool(
        re.search(r'prefers-color-scheme:\s*dark\s*\)\s*\{[^}]*:root:not\(\[data-theme="light"\]\)', stripped, re.DOTALL)
    )
    has_explicit_dark = bool(re.search(r':root\[data-theme="dark"\]\s*\{', stripped))
    check("prefers-color-scheme dark block present", has_media_dark)
    check("[data-theme=dark] override block present", has_explicit_dark)

    body_bg = re.search(r"\bbody\s*\{[^}]*background\s*:\s*var\(--", stripped, re.DOTALL)
    check("body sets background from a token", bool(body_bg))

    chapters = _load_json("maps.json")["chapters"]
    entry = next((c for c in chapters if str(c["number"]) == chapter_num), None)
    if entry is None:
        check("title matches maps.json", False, f"no chapter {chapter_num} in maps.json")
    else:
        expected_title = entry["artifact_title"]
        title_match = re.search(r"<title>(.*?)</title>", stripped, re.DOTALL)
        actual = title_match.group(1).strip() if title_match else None
        check("title matches maps.json exactly", actual == expected_title, f"got {actual!r}, want {expected_title!r}")

    script_positions = []
    for script in KATEX_SCRIPTS_IN_ORDER:
        m = re.search(re.escape(script), stripped)
        script_positions.append(m.start() if m else None)
    all_present = all(p is not None for p in script_positions)
    in_order = all_present and script_positions == sorted(script_positions)
    check("KaTeX + mhchem + auto-render scripts present", all_present, str(script_positions))
    check("KaTeX scripts in required order", in_order)

    render_call = re.search(r'getElementById\(["\'](.+?)["\']\)', stripped)
    if render_call:
        target_id = render_call.group(1)
        id_exists = bool(re.search(rf'id=["\']{ re.escape(target_id) }["\']', stripped))
        check("renderMathInElement target id exists in document", id_exists, target_id)
    else:
        check("renderMathInElement target id exists in document", False, "no getElementById call found")

    # The on-page marker for a first-contact term is the exposure-tag span
    # (chem/template.html / chem/SKILL.md section 1), not literal "[exposure]"
    # text -- count real usages, not the spec's own name for the tag.
    exposure_count = len(re.findall(r'class="exposure-tag"', stripped))
    if chapter_num in FIRST_CONTACT_CHAPTERS:
        check("first-contact chapter: exposure-tag spans present", exposure_count > 0, f"{exposure_count} found")
    else:
        check("theory-known chapter: no exposure-tag spans", exposure_count == 0, f"{exposure_count} found")

    in_this_video = re.search(r"\bin this video\b", stripped, re.IGNORECASE)
    check('no sentence begins "In this video"', not bool(in_this_video))

    size_mb = len(html.encode("utf-8")) / (1024 * 1024)
    check("file under 16 MB", size_mb < 16, f"{size_mb:.2f} MB")

    if expect_pyq:
        has_pyq_marker = bool(re.search(r"question types|repeat offenders|mark slot", stripped, re.IGNORECASE))
        check("PYQ section present (expected)", has_pyq_marker)
    else:
        check("PYQ section correctly absent (not expected yet)", True, "skip: --stage lecture")

    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("html_path", type=Path)
    parser.add_argument(
        "--stage",
        choices=["lecture", "pyq", "final"],
        default="final",
        help="lecture: only the lecture section exists yet. pyq: only the PYQ section exists "
             "yet. final: both should be present (default).",
    )
    args = parser.parse_args()

    html = args.html_path.read_text(encoding="utf-8")
    chapter_num = _chapter_number_from_filename(args.html_path)
    expect_pyq = args.stage in ("pyq", "final")

    results = run_checks(html, chapter_num, expect_pyq)
    failed = [r for r in results if not r[1]]

    for name, passed, detail in results:
        mark = "PASS" if passed else "FAIL"
        line = f"[{mark}] {name}"
        if detail and not passed:
            line += f" -- {detail}"
        print(line)

    print(f"\n{len(results) - len(failed)}/{len(results)} checks passed.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
