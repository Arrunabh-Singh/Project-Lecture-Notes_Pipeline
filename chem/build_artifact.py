"""Splice a chapter's written content into chem/template.html.

Keeps the template as the single source of the design system (token cascade,
fonts, inlined KaTeX CSS, the three scripts in their required order) so every
chapter artifact is identical below the content, and only the content differs.

Usage:
    python3 chem/build_artifact.py <content.html> --chapter 2

Writes chem/build/ch<N>.html. Run chem/qa.py on the result before publishing.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

CHEM_DIR = Path(__file__).resolve().parent

# Classes the chapter content uses that the template doesn't already define.
# Kept here rather than in template.html so the template stays the artifact
# skeleton and these stay clearly "additions the notes needed".
EXTRA_CSS = """
.lede {
  font-size: 1.02rem; line-height: 1.6; color: var(--text-muted);
  margin: 0.6rem 0 0; text-wrap: pretty;
}
.asks {
  margin: 0.9rem 0 0; padding: 0.6rem 0.75rem;
  border-left: 3px solid var(--accent); background: var(--accent-soft);
  border-radius: 0 5px 5px 0; font-size: 0.94rem; color: var(--text);
}
.note {
  font-size: 0.88rem; color: var(--text-muted); font-style: italic;
  margin: 0 0 0.9rem;
}
footer {
  margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid var(--border);
  font-size: 0.84rem; color: var(--text-muted); line-height: 1.55;
}
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("content_path", type=Path)
    parser.add_argument("--chapter", required=True)
    args = parser.parse_args()

    maps = json.loads((CHEM_DIR / "maps.json").read_text(encoding="utf-8"))
    entry = next((c for c in maps["chapters"] if str(c["number"]) == args.chapter), None)
    if entry is None:
        raise SystemExit(f"chapter {args.chapter} not in chem/maps.json")

    tpl = (CHEM_DIR / "template.html").read_text(encoding="utf-8")
    content = args.content_path.read_text(encoding="utf-8")

    tpl = tpl.replace("<title>{{ARTIFACT_TITLE}}</title>",
                      f"<title>{entry['artifact_title']}</title>")

    idx = tpl.rindex("</style>")
    tpl = tpl[:idx] + EXTRA_CSS + tpl[idx:]

    start = tpl.index('<main id="chem-content">') + len('<main id="chem-content">')
    end = tpl.index("</main>")
    out = tpl[:start] + "\n" + content + "\n" + tpl[end:]

    out_path = CHEM_DIR / "build" / f"ch{args.chapter}.html"
    out_path.write_text(out, encoding="utf-8")
    print(f"wrote {out_path} ({len(out)} bytes) — title: {entry['artifact_title']}")


if __name__ == "__main__":
    main()
