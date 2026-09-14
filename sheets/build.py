"""Splice written content into sheets/template.html and write sheets/build/<name>.html.

Sibling of chem/build_artifact.py, but for the four cross-chapter revision
sheets rather than a per-chapter artifact. Two differences from that script:

  - The 359 KB of inlined KaTeX CSS lives in exactly one place
    (lecturepipe/publish/static/katex-inline.css) and is spliced in here at
    build time, instead of being pasted into the template. The template stays
    readable and the repo stores one copy rather than one per sheet.
  - The accent pair is substituted per sheet from sheets/maps.json, so the
    chemistry sheets inherit the teal already used by the six published
    chemistry chapter artifacts and the physics sheets get their own indigo.
    Substituting real hex values here (rather than layering a
    [data-subject] override in CSS) keeps every token literal inside the
    three :root blocks, which is what sheets/qa.py checks.

Usage:
    python3 sheets/build.py <content.html> --name chem-formulas
    python3 sheets/build.py <content.html>          # name inferred from filename stem
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SHEETS_DIR = Path(__file__).resolve().parent
ROOT = SHEETS_DIR.parent
KATEX_CSS = ROOT / "lecturepipe" / "publish" / "static" / "katex-inline.css"


def load_sheet(name: str) -> dict:
    maps = json.loads((SHEETS_DIR / "maps.json").read_text(encoding="utf-8"))
    entry = next((s for s in maps["sheets"] if s["name"] == name), None)
    if entry is None:
        known = ", ".join(s["name"] for s in maps["sheets"])
        raise SystemExit(f"sheet {name!r} not in sheets/maps.json (known: {known})")
    return entry


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("content_path", type=Path, help="HTML fragment to splice in")
    parser.add_argument(
        "--name",
        help="sheet name from sheets/maps.json; defaults to the content file's stem "
             "with a trailing _content stripped",
    )
    args = parser.parse_args()

    name = args.name
    if not name:
        name = args.content_path.stem
        for suffix in ("_content", "-content"):
            if name.endswith(suffix):
                name = name[: -len(suffix)]
    entry = load_sheet(name)

    tpl = (SHEETS_DIR / "template.html").read_text(encoding="utf-8")
    content = args.content_path.read_text(encoding="utf-8")

    # Order matters: KaTeX CSS goes in first and is never scanned for slots,
    # so a stray {{...}} inside it (there are none today) could not be
    # mistaken for a template slot by a later replacement.
    for slot, value in (
        ("{{ARTIFACT_TITLE}}", entry["artifact_title"]),
        ("{{ACCENT_LIGHT}}", entry["accent_light"]),
        ("{{ACCENT_SOFT_LIGHT}}", entry["accent_soft_light"]),
        ("{{ACCENT_DARK}}", entry["accent_dark"]),
        ("{{ACCENT_SOFT_DARK}}", entry["accent_soft_dark"]),
    ):
        if slot not in tpl:
            raise SystemExit(f"template is missing the {slot} slot")
        tpl = tpl.replace(slot, value)

    tpl = tpl.replace("{{KATEX_CSS}}", KATEX_CSS.read_text(encoding="utf-8"))
    tpl = tpl.replace("{{CONTENT}}", content)

    # Match the slot syntax specifically, not a bare "{{"/"}}" pair: nested
    # LaTeX braces produce "}}" all over a maths-heavy page (\text{ in mol L}^{-1}}),
    # so a naive substring check reports every real page as broken.
    # Strip HTML comments first -- the template's own authoring comment says
    # "Slots are {{LIKE_THIS}}", which is documentation, not an unfilled slot.
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", re.sub(r"<!--.*?-->", "", tpl, flags=re.DOTALL))
    if leftover:
        raise SystemExit(f"template still has unfilled slots after substitution: {sorted(set(leftover))}")

    out_dir = SHEETS_DIR / "build"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{name}.html"
    out_path.write_text(tpl, encoding="utf-8")
    print(f"wrote {out_path} ({len(tpl):,} bytes) — title: {entry['artifact_title']}")


if __name__ == "__main__":
    main()
