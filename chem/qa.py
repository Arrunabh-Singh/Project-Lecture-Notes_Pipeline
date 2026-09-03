#!/usr/bin/env python3
"""Pre-publish QA for chemistry artifacts -- scripts the checklist in
chem/SKILL.md section 10 so it doesn't have to be re-read into a model's
context by eye on every one of the 12 videos.

Usage: python3 chem/qa.py chem/build/ch4-oneshot.html [more files...]
       python3 chem/qa.py chem/build/*.html

Exits 0 if every file passes every check, 1 otherwise. Chapter number and
video type are read from the filename: ch<N>-<pyq|oneshot>.html.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAPS = json.loads((ROOT / "maps.json").read_text())
CHAPTERS = {c["number"]: c for c in MAPS["chapters"]}
FIRST_CONTACT = set(int(n) for n in MAPS["prior_knowledge"]["first_contact"])

FILENAME_RE = re.compile(r"ch(\d+)-(pyq|oneshot)\.html$")

MAX_BYTES = 16 * 1024 * 1024


def _strip_comments(html: str) -> str:
    # Explanatory comments in template.html contain literal tag-looking
    # text ("Do not add <!doctype>, <html>...") -- strip comments first so
    # those never masquerade as real tags or real content.
    return re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)


def _root_token_defs(html: str) -> set[str]:
    m = re.search(r":root\s*\{([^}]*)\}", html, flags=re.DOTALL)
    if not m:
        return set()
    return set(re.findall(r"(--[\w-]+)\s*:", m.group(1)))


def _used_tokens(html: str) -> set[str]:
    return set(re.findall(r"var\((--[\w-]+)\)", html))


def check_file(path: Path) -> list[tuple[str, bool, str]]:
    """Returns list of (check_name, passed, detail)."""
    name_match = FILENAME_RE.search(path.name)
    results: list[tuple[str, bool, str]] = []

    if not name_match:
        return [("filename matches ch<N>-<pyq|oneshot>.html", False, path.name)]

    chapter_num = int(name_match.group(1))
    video_type = name_match.group(2)
    chapter = CHAPTERS.get(chapter_num)
    if chapter is None:
        return [("chapter number is in maps.json", False, str(chapter_num))]

    raw = path.read_text(encoding="utf-8")
    html = _strip_comments(raw)

    def add(name: str, passed: bool, detail: str = "") -> None:
        results.append((name, passed, detail))

    # 1. No wrapper tags.
    wrapper_hits = re.findall(r"<!doctype|<html[\s>]|<head[\s>]|<body[\s>]", html, flags=re.IGNORECASE)
    add("no <!doctype/html/head/body> wrapper tags", not wrapper_hits, str(wrapper_hits))

    # 2. No top-level <details> with `open`.
    open_details = re.findall(r"<details\b[^>]*\bopen\b", html, flags=re.IGNORECASE)
    add("no top-level <details open>", not open_details, str(len(open_details)))

    # 3. Every var(--token) used is defined in the bare :root block.
    defined = _root_token_defs(html)
    used = _used_tokens(html)
    missing = sorted(used - defined)
    add("every var(--token) is defined in :root", not missing, str(missing))

    # 4. Both dark blocks present.
    has_media_dark = bool(re.search(r'@media\s*\(prefers-color-scheme:\s*dark\)', html))
    has_attr_dark = bool(re.search(r':root\[data-theme=["\']dark["\']\]', html))
    add("prefers-color-scheme dark block present", has_media_dark)
    add('[data-theme="dark"] block present', has_attr_dark)

    # 5. body sets background from a token.
    body_bg = re.search(r"body\s*\{[^}]*background[^:]*:\s*var\(--[\w-]+\)", html, flags=re.DOTALL)
    add("body background set from a var() token", bool(body_bg))

    # 6. <title> matches maps.json exactly.
    title_field = "pyq_title" if video_type == "pyq" else "oneshot_title"
    expected_title = chapter[title_field]
    title_match = re.search(r"<title>(.*?)</title>", raw, flags=re.DOTALL)
    actual_title = title_match.group(1).strip() if title_match else None
    add("<title> matches maps.json exactly", actual_title == expected_title,
        f"expected {expected_title!r}, got {actual_title!r}")

    # 7. KaTeX CSS inlined + three scripts in required order.
    has_katex_css = ".katex" in html
    add("KaTeX CSS inlined (.katex selectors present)", has_katex_css)
    script_srcs = re.findall(r'<script[^>]+src="([^"]+)"', raw)
    katex_idx = next((i for i, s in enumerate(script_srcs) if "katex.min.js" in s and "mhchem" not in s), None)
    mhchem_idx = next((i for i, s in enumerate(script_srcs) if "mhchem" in s), None)
    autorender_idx = next((i for i, s in enumerate(script_srcs) if "auto-render" in s), None)
    order_ok = (
        katex_idx is not None and mhchem_idx is not None and autorender_idx is not None
        and katex_idx < mhchem_idx < autorender_idx
    )
    add("katex -> mhchem -> auto-render script order", order_ok, str(script_srcs))

    # 8. renderMathInElement targets a container id that exists.
    target_match = re.search(r'getElementById\(["\']([\w-]+)["\']\)', html)
    target_id = target_match.group(1) if target_match else None
    id_exists = bool(target_id and re.search(rf'id="{re.escape(target_id)}"', html))
    add("renderMathInElement target id exists in document", id_exists, str(target_id))

    # Content-only view: CSS rules like ".exposure-tag { ... }" contain the
    # same substrings as real usage, so tag/heading checks below must look
    # only inside <main>, never in the <style> blocks.
    main_match = re.search(r"<main\b[^>]*>(.*)</main>", html, flags=re.DOTALL)
    content = main_match.group(1) if main_match else ""

    # 9/10. exposure tag presence rule (content only, not the CSS definition).
    has_exposure = '<span class="exposure-tag"' in content or "[exposure]" in content
    if chapter_num in FIRST_CONTACT:
        add("Ch4/5/6: at least one [exposure] tag present", has_exposure)
    else:
        add("Ch1/2/3: no [exposure] tags present", not has_exposure)

    if video_type == "pyq":
        # 11. All four PYQ parts present, in order.
        headings = re.findall(r"<summary>\s*(?:<[^>]+>)?\s*(\d)\.", content)
        add("PYQ: four numbered parts present in order 1-4", headings == ["1", "2", "3", "4"], str(headings))

        # 12. Each numerical type: exactly one .worked block, rest answer-only.
        numerical_section = re.search(r"Numerical types.*?</section>", content, flags=re.DOTALL)
        if numerical_section:
            worked_count = len(re.findall(r'class="worked"', numerical_section.group(0)))
            coldq_count = len(re.findall(r'class="cold-q"', numerical_section.group(0)))
            add("PYQ numerical section has worked + cold-q items", worked_count >= 1 and coldq_count >= 1,
                f"worked={worked_count} cold-q={coldq_count}")
        else:
            add("PYQ: 'Numerical types' section found", False)

    # 13. No leftover template placeholders.
    leftover = re.findall(r"\{\{[A-Z0-9_]+\}\}", html)
    add("no unfilled {{PLACEHOLDER}} tokens remain", not leftover, str(sorted(set(leftover))[:5]))

    # 14. No "In this video" sentence.
    add('no sentence starts "In this video"', "in this video" not in html.lower())

    # 15. File size.
    size = path.stat().st_size
    add(f"file under 16 MB (actual {size / 1024:.0f} KB)", size < MAX_BYTES)

    return results


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1
    all_passed = True
    for arg in argv:
        path = Path(arg)
        print(f"\n=== {path.name} ===")
        for check_name, passed, detail in check_file(path):
            mark = "PASS" if passed else "FAIL"
            line = f"  [{mark}] {check_name}"
            if not passed and detail:
                line += f"  -- {detail}"
            print(line)
            if not passed:
                all_passed = False
    print()
    print("ALL CHECKS PASSED" if all_passed else "SOME CHECKS FAILED")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
