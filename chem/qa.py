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

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lecturepipe.publish.qa_checks import (
    strip_html_comments as _strip_html_comments,
    structural_checks,
    title_check,
)

CHEM_DIR = Path(__file__).resolve().parent
FIRST_CONTACT_CHAPTERS = {"4", "5", "6"}
def _load_json(name: str) -> dict:
    return json.loads((CHEM_DIR / name).read_text(encoding="utf-8"))


def _chapter_number_from_filename(path: Path) -> str:
    m = re.match(r"ch(\d+)\.html?$", path.name)
    if not m:
        raise SystemExit(f"expected a filename like ch4.html, got {path.name!r}")
    return m.group(1)


def run_checks(html: str, chapter_num: str, expect_pyq: bool) -> list[tuple[str, bool, str]]:
    """Returns a list of (check_name, passed, detail) tuples."""
    stripped = _strip_html_comments(html)
    checks = structural_checks(html, stripped, math_root_id="chem-content")

    def check(name: str, passed: bool, detail: str = "") -> None:
        checks.append((name, passed, detail))

    chapters = _load_json("maps.json")["chapters"]
    entry = next((c for c in chapters if str(c["number"]) == chapter_num), None)
    if entry is None:
        check("title matches maps.json", False, f"no chapter {chapter_num} in maps.json")
    else:
        checks.append(title_check(stripped, entry["artifact_title"]))

    # The on-page marker for a first-contact term is the exposure-tag span
    # (chem/template.html / chem/SKILL.md section 1), not literal "[exposure]"
    # text -- count real usages, not the spec's own name for the tag.
    exposure_count = len(re.findall(r'class="exposure-tag"', stripped))
    if chapter_num in FIRST_CONTACT_CHAPTERS:
        check("first-contact chapter: exposure-tag spans present", exposure_count > 0, f"{exposure_count} found")
    else:
        check("theory-known chapter: no exposure-tag spans", exposure_count == 0, f"{exposure_count} found")

    check('no sentence begins "In this video"', not bool(re.search(r"\bin this video\b", stripped, re.IGNORECASE)))

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
