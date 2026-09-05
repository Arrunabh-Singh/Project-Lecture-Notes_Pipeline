"""Pre-publish QA for the four cross-chapter revision sheets.

Shares the structural checks with chem/qa.py via
lecturepipe/publish/qa_checks.py, and adds the rules that are specific to
these pages:

  - a formula sheet's entries must each carry a unit slot. The unit is the
    whole point of a physics/chemistry formula sheet; an entry without one
    is the failure mode this check exists to catch.
  - a derivation must end somewhere: every block needs a result box, and
    (since the user asked for real drawn figures rather than prose
    descriptions) an inline <svg>.
  - SVG <marker> ids must be unique across the page. Roughly fifty figures
    on one page each defining an arrowhead is the exact situation where a
    generic id="arrow" silently makes every figure after the first use the
    first one's marker.
  - no hard-coded stroke/fill colour inside an SVG. currentColor is what
    makes a figure legible in both themes; a literal hex disappears against
    one of the two grounds.

Usage:
    python3 sheets/qa.py sheets/build/chem-formulas.html
Exit code is 0 iff every check passes.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lecturepipe.publish.qa_checks import (  # noqa: E402
    report,
    strip_html_comments,
    structural_checks,
    title_check,
)

SHEETS_DIR = Path(__file__).resolve().parent

# Colour literals are legal inside the inlined KaTeX stylesheet and the three
# :root token blocks; this pattern only looks inside <svg> elements.
_HEX = re.compile(r'(?:stroke|fill)\s*=\s*["\']#[0-9A-Fa-f]{3,8}["\']')


def load_sheet(name: str) -> dict:
    maps = json.loads((SHEETS_DIR / "maps.json").read_text(encoding="utf-8"))
    entry = next((s for s in maps["sheets"] if s["name"] == name), None)
    if entry is None:
        raise SystemExit(f"sheet {name!r} not in sheets/maps.json")
    return entry


def run_checks(html: str, entry: dict) -> list[tuple[str, bool, str]]:
    stripped = strip_html_comments(html)
    checks = structural_checks(html, stripped, math_root_id="sheet-root")

    def check(name: str, passed: bool, detail: str = "") -> None:
        checks.append((name, passed, detail))

    checks.append(title_check(stripped, entry["artifact_title"]))

    svgs = re.findall(r"<svg\b.*?</svg>", stripped, re.DOTALL)
    marker_ids = re.findall(r"<marker\b[^>]*\bid=[\"']([^\"']+)[\"']", stripped)
    dupes = [i for i, n in Counter(marker_ids).items() if n > 1]
    check("SVG marker ids unique across the page", not dupes, f"duplicated: {dupes}" if dupes else f"{len(marker_ids)} markers")

    hard_coded = [m for svg in svgs for m in _HEX.findall(svg)]
    check(
        "no hard-coded stroke/fill colour inside an SVG",
        not hard_coded,
        f"{len(hard_coded)} found — use currentColor" if hard_coded else "",
    )

    if svgs:
        unlabelled = [s for s in svgs if "aria-label" not in s]
        check("every SVG has an aria-label", not unlabelled, f"{len(unlabelled)} without")
        no_viewbox = [s for s in svgs if "viewBox" not in s]
        check("every SVG has a viewBox", not no_viewbox, f"{len(no_viewbox)} without")

    if entry["kind"] == "formulas":
        entries = re.findall(r"<details class=\"f\".*?</details>", stripped, re.DOTALL)
        check("formula entries found", len(entries) > 0, f"{len(entries)} entries")
        no_unit = [e for e in entries if 'class="unit"' not in e]
        check(
            "every formula entry carries a unit slot",
            not no_unit,
            f"{len(no_unit)} of {len(entries)} entries have no td.unit",
        )
        check(
            "recognise index present",
            bool(re.search(r'class="rx-row"', stripped)),
        )
        instant = len(re.findall(r'class="dot"', stripped))
        slow = len(re.findall(r'class="dot slow"', stripped))
        check(
            "instantness marking is discriminating",
            slow > 0 and instant > 0,
            f"{instant} must-be-instant, {slow} slower — a sheet where everything is starred is useless",
        )
    else:
        # Each block opens <div class="deriv" id="D7"> -- match the class
        # attribute allowing anything after it, and take each block as running
        # up to the next one (or the end of the document).
        starts = [m.start() for m in re.finditer(r'<div class="deriv"[ >]', stripped)]
        blocks = [
            stripped[s : (starts[i + 1] if i + 1 < len(starts) else len(stripped))]
            for i, s in enumerate(starts)
        ]
        check("derivation blocks found", len(blocks) > 0, f"{len(blocks)} blocks")
        no_result = [b for b in blocks if 'class="result"' not in b]
        check("every derivation has a result box", not no_result, f"{len(no_result)} without")
        no_fig = [b for b in blocks if "<svg" not in b]
        check("every derivation has a drawn figure", not no_fig, f"{len(no_fig)} without an inline SVG")
        no_steps = [b for b in blocks if 'class="steps"' not in b]
        check("every derivation has numbered steps", not no_steps, f"{len(no_steps)} without")

    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("html_path", type=Path)
    parser.add_argument("--name", help="sheet name; defaults to the filename stem")
    args = parser.parse_args()

    entry = load_sheet(args.name or args.html_path.stem)
    html = args.html_path.read_text(encoding="utf-8")
    sys.exit(0 if report(run_checks(html, entry)) else 1)


if __name__ == "__main__":
    main()
