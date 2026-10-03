"""Render the Markdown export to plain, readable PDFs.

One PDF per chapter, plus the cross-chapter sheets, plus a combined volume
per subject. The container has no pandoc and no LaTeX, so the path is
Markdown -> HTML -> Chromium print-to-PDF via Playwright, with KaTeX
vendored locally (pdfbuild/static/) because a file:// page cannot reach a CDN.

Two readers have to be served at once, and they want opposite things:

  a human wants the maths typeset -- a real fraction bar, a real square root;
  a machine wants the maths as text it can parse back out of the PDF.

So every equation is printed twice. KaTeX typesets it, and the LaTeX source
is emitted next to it inside a <span class="tex-src">, which the print
stylesheet renders at zero size in a colour that never shows. It costs
nothing on the page and it survives into the PDF's text layer, so
pdftotext-style extraction reads back the original TeX.

Usage:
    python3 tools/build_pdfs.py                 # everything
    python3 tools/build_pdfs.py --only ch5      # one document, for iterating
    python3 tools/build_pdfs.py --no-combined   # skip the two big volumes
"""
from __future__ import annotations

import argparse
import html as htmllib
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "markdown"
STATIC = ROOT / "pdfbuild" / "static"
OUT = ROOT / "pdf"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_markdown import PHYS_CHAPTERS, rebase, strip_h1  # noqa: E402

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# ------------------------------------------------------------------ maths

# NOT \x02/\x03 -- python-markdown uses STX/ETX for its own placeholders
# and silently eats anything that looks like one.
_TOKEN = "qqmathqq{}qqdneqq"
_TOKEN_RE = re.compile(r"qqmathqq(\d+)qqdneqq")
# $$...$$ first, then single-$ spans that are not part of a $$ pair
_DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_INLINE = re.compile(r"(?<!\$)\$([^$\n]+?)\$(?!\$)")


def protect_math(md_text: str) -> tuple[str, list[tuple[bool, str]]]:
    """Pull every maths span out before Markdown gets a chance to eat it.

    Markdown treats _ as emphasis and \\ as an escape, so a subscript or a
    \\frac left in the text comes out mangled. Placeholders go in, the
    original TeX comes back after conversion.
    """
    spans: list[tuple[bool, str]] = []

    def take(display: bool):
        def sub(m: re.Match) -> str:
            spans.append((display, m.group(1)))
            return _TOKEN.format(len(spans) - 1)
        return sub

    md_text = _DISPLAY.sub(take(True), md_text)
    md_text = _INLINE.sub(take(False), md_text)
    return md_text, spans


def restore_math(html_text: str, spans: list[tuple[bool, str]]) -> str:
    def sub(m: re.Match) -> str:
        display, tex = spans[int(m.group(1))]
        esc = htmllib.escape(tex)
        d = "$$" if display else "$"
        cls = "eq" if display else "im"
        # The typeset copy and the extractable copy, in that order.
        return (f'<span class="{cls}">{d}{esc}{d}</span>'
                f'<span class="tex-src">{d}{esc}{d}</span>')
    return _TOKEN_RE.sub(sub, html_text)


# ------------------------------------------------------------------ shell

STYLE = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
* { box-sizing: border-box; }
body {
  font-family: "DejaVu Serif", Georgia, serif;
  font-size: 10.5pt; line-height: 1.5; color: #000; background: #fff;
  margin: 0; -webkit-print-color-adjust: exact;
}
h1, h2, h3, h4, h5, h6 {
  font-family: "DejaVu Sans", Helvetica, Arial, sans-serif;
  color: #000; line-height: 1.25; margin: 1.1em 0 .35em; page-break-after: avoid;
}
h1 { font-size: 19pt; margin-top: 0; }
h2 { font-size: 14pt; border-bottom: 1.5pt solid #000; padding-bottom: .18em; margin-top: 1.6em; }
h3 { font-size: 12pt; margin-top: 1.3em; }
h4 { font-size: 10.5pt; margin-top: 1.1em; }
h5, h6 { font-size: 10pt; font-style: italic; font-weight: 600; }
h2 + h3, h3 + h4 { margin-top: .6em; }
p { margin: .5em 0; orphans: 2; widows: 2; }
ul { margin: .5em 0; padding-left: 1.4em; }
/* two-digit step numbers clip at 1.5em -- derivations run past ten steps */
ol { margin: .5em 0; padding-left: 2.3em; }
li { margin: .22em 0; }
a { color: #000; text-decoration: none; }
blockquote {
  margin: .6em 0; padding: .1em 0 .1em .8em;
  border-left: 2pt solid #888; color: #222;
}
blockquote p { margin: .3em 0; }
code, kbd { font-family: "DejaVu Sans Mono", monospace; font-size: .88em; }
hr { border: 0; border-top: .75pt solid #bbb; margin: 1.4em 0; }
table {
  border-collapse: collapse; width: 100%; margin: .7em 0;
  font-size: 9.5pt; page-break-inside: avoid;
}
th, td { border: .5pt solid #999; padding: .3em .45em; text-align: left; vertical-align: top; }
th { background: #eee; font-family: "DejaVu Sans", sans-serif; font-size: 9pt; }
strong { font-weight: 700; }

/* the maths pair: one copy typeset, one copy invisible but extractable */
.katex { font-size: 1.02em; }
.katex-display { margin: .55em 0; page-break-inside: avoid; }
.tex-src { font-size: .12pt; line-height: 0; color: #ffffff; }

.docmeta {
  font-family: "DejaVu Sans", sans-serif; font-size: 8.5pt; color: #444;
  border-bottom: .5pt solid #bbb; padding-bottom: .5em; margin-bottom: 1.4em;
}
.chapter-break { page-break-before: always; }
"""

FOOTER = ('<div style="width:100%;font:7.5pt \'DejaVu Sans\',sans-serif;color:#666;'
          'padding:0 16mm;display:flex;justify-content:space-between;">'
          '<span>{label}</span><span class="pageNumber"></span></div>')

SHELL = """<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<style>{katex_css}</style>
<style>{style}</style>
</head><body>
<div class="docmeta">{meta}</div>
{body}
<script>{katex_js}</script>
<script>{mhchem_js}</script>
<script>{autorender_js}</script>
<script>
document.addEventListener("DOMContentLoaded", function () {{
  renderMathInElement(document.body, {{
    delimiters: [
      {{ left: "$$", right: "$$", display: true }},
      {{ left: "$", right: "$", display: false }}
    ],
    ignoredClasses: ["tex-src"],
    throwOnError: false
  }});
  window.__mathDone = true;
}});
</script>
</body></html>"""


def read_static() -> dict[str, str]:
    return {
        "katex_css": (STATIC / "katex.css").read_text(encoding="utf-8"),
        "katex_js": (STATIC / "katex.min.js").read_text(encoding="utf-8"),
        "mhchem_js": (STATIC / "mhchem.min.js").read_text(encoding="utf-8"),
        "autorender_js": (STATIC / "auto-render.min.js").read_text(encoding="utf-8"),
    }


def md_to_html(md_text: str) -> str:
    protected, spans = protect_math(md_text)
    body = markdown.markdown(
        protected,
        extensions=["tables", "sane_lists", "attr_list"],
        output_format="html5",
    )
    return restore_math(body, spans)


# ------------------------------------------------------------------ docs

PROVENANCE = ("Built from the teacher's recorded lectures, transcribed and "
              "checked against the board frames and the NCERT text. "
              "Figures appear as prose descriptions.")


def collect() -> list[dict]:
    """Every PDF to build: key, subject, filename, title, meta line, markdown."""
    docs: list[dict] = []

    chem_titles = {
        "01-solutions": ("Solutions", "Chapter 1 · 15 marks"),
        "02-electrochemistry": ("Electrochemistry", "Chapter 2 · 14 marks"),
        "03-chemical-kinetics": ("Chemical Kinetics", "Chapter 3 · 13 marks"),
        "04-d-and-f-block": ("The d- and f-Block Elements", "Chapter 4 · 11 marks"),
        "05-coordination-compounds": ("Coordination Compounds", "Chapter 5 · 11 marks"),
        "06-haloalkanes-and-haloarenes": ("Haloalkanes and Haloarenes", "Chapter 6 · 6 marks"),
    }
    for stem, (title, sub) in chem_titles.items():
        src = MD / "chemistry" / "chapters" / f"{stem}.md"
        docs.append(dict(key=stem, subject="chemistry", stem=stem, title=title,
                         meta=f"Class XII CBSE Chemistry · {sub} · {PROVENANCE}",
                         md=src.read_text(encoding="utf-8")))

    for stem, title, sub in [
        ("every-chemistry-formula", "Every Chemistry Formula",
         "All six chapters · 50 entries with symbols, units, cue and trap"),
        ("chemistry-derived", "Chemistry, Derived",
         "All six chapters · 12 derivations"),
    ]:
        docs.append(dict(key=stem, subject="chemistry", stem=stem, title=title,
                         meta=f"Class XII CBSE Chemistry · {sub}",
                         md=(MD / "chemistry" / f"{stem}.md").read_text(encoding="utf-8")))

    for chap_dir in sorted((MD / "physics" / "chapter-notes").glob("leph1*")):
        label = PHYS_CHAPTERS.get(chap_dir.name, chap_dir.name)
        num, name = label.split(" · ", 1)
        notes = sorted(chap_dir.glob("*.md"))
        parts = [rebase(p.read_text(encoding="utf-8"), 2) for p in notes]
        stem = f"{num.split()[-1].zfill(2)}-{name.lower().replace(' ', '-')}"
        docs.append(dict(key=chap_dir.name, subject="physics", stem=stem, title=name,
                         meta=f"Class XII CBSE Physics · {num} · {len(notes)} lectures · {PROVENANCE}",
                         md="\n\n".join(parts)))

    for stem, title, sub in [
        ("every-physics-formula", "Every Physics Formula",
         "Chapters 1-9 · 100 entries with symbols, units, cue and trap"),
        ("physics-derived", "Physics, Derived",
         "Chapters 1-9 · 45 derivations, PD1-PD45"),
    ]:
        docs.append(dict(key=stem, subject="physics", stem=stem, title=title,
                         meta=f"Class XII CBSE Physics · {sub}",
                         md=(MD / "physics" / f"{stem}.md").read_text(encoding="utf-8")))

    for fname, title, sub in [
        ("ray-optics-to-9-4.md", "Ray Optics to 9.4",
         "Chapter 9 · written from NCERT; these lectures were never transcribed"),
        ("alternating-current-in-eight-derivations.md", "Alternating Current in Eight Derivations",
         "Chapter 7 · theory, eight derivations, formula strip, question tiers"),
        ("electromagnetic-waves-for-six-marks.md", "Electromagnetic Waves for Six Marks",
         "Chapter 8 · theory, five derivations, formula strip, question tiers"),
    ]:
        docs.append(dict(key=fname[:-3], subject="physics", stem=fname[:-3], title=title,
                         meta=f"Class XII CBSE Physics · {sub}",
                         md=(MD / "physics" / "pages" / fname).read_text(encoding="utf-8")))

    return docs


def combined(docs: list[dict], subject: str) -> dict:
    parts = []
    for i, d in enumerate(docs):
        if d["subject"] != subject:
            continue
        cls = ' class="chapter-break"' if parts else ""
        parts.append(f'<h1{cls}>{htmllib.escape(d["title"])}</h1>\n\n'
                     + rebase(strip_h1(d["md"]), 2))
    name = subject.capitalize()
    return dict(key=f"all-{subject}", subject=subject, stem=f"00-all-{name.lower()}",
                title=f"{name} — Everything", raw_html_head=True,
                meta=f"Class XII CBSE {name} · every chapter and sheet in one file · {PROVENANCE}",
                md="\n\n".join(parts))


# ------------------------------------------------------------------ render

def build(docs: list[dict]) -> list[Path]:
    from playwright.sync_api import sync_playwright

    static = read_static()
    written: list[Path] = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROME)
        page = browser.new_page()
        for d in docs:
            body = md_to_html(d["md"])
            if not body.lstrip().startswith("<h1"):
                body = f'<h1>{htmllib.escape(d["title"])}</h1>\n' + body
            doc = SHELL.format(title=d["title"], meta=htmllib.escape(d["meta"]),
                               style=STYLE, body=body, **static)
            tmp = OUT / f".{d['stem']}.html"
            tmp.write_text(doc, encoding="utf-8")
            page.goto(tmp.resolve().as_uri(), wait_until="load")
            page.wait_for_function("window.__mathDone === true", timeout=120_000)
            dest = OUT / d["subject"] / f"{d['stem']}.pdf"
            dest.parent.mkdir(parents=True, exist_ok=True)
            page.pdf(path=str(dest), format="A4", print_background=True,
                     display_header_footer=True, header_template="<span></span>",
                     footer_template=FOOTER.format(label=htmllib.escape(d["title"])),
                     margin={"top": "16mm", "bottom": "18mm", "left": "16mm", "right": "16mm"})
            tmp.unlink()
            print(f"  {dest.relative_to(ROOT)}  ({dest.stat().st_size/1024:.0f} KB)")
            written.append(dest)
        browser.close()
    return written


def write_index(docs: list[dict], written: list[Path]) -> None:
    from pypdf import PdfReader
    pages = {p: len(PdfReader(str(p)).pages) for p in written}
    lines = [
        "# PDFs", "",
        "Every physics and chemistry page in this project, as plain A4 PDFs.",
        "Generated by `tools/build_pdfs.py` from `markdown/` — rebuild rather than edit.",
        "",
        "Maths is typeset with KaTeX so a person reads a real fraction bar. The LaTeX",
        "source of every equation is also written into the PDF at zero visible size, so",
        "text extraction gives back `$\\frac{1}{4\\pi\\varepsilon_0}$` rather than glyph soup —",
        "the file reads correctly for a person and for a machine.",
        "",
        "`00-all-*.pdf` is that whole subject in one file; the rest are one per chapter or sheet.",
        "",
    ]
    for subject in ("physics", "chemistry"):
        lines += [f"## {subject.capitalize()}", "",
                  "| Document | Pages | File |", "|---|---|---|"]
        for d in docs:
            if d["subject"] != subject:
                continue
            path = OUT / subject / f"{d['stem']}.pdf"
            if path in pages:
                rel = path.relative_to(OUT).as_posix()
                lines.append(f"| {d['title']} | {pages[path]} | [`{rel}`]({rel}) |")
        lines.append("")
    total = sum(pages.values())
    lines.append(f"**{len(written)} PDFs, {total} pages.**")
    (OUT / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="build just the document with this key")
    ap.add_argument("--no-combined", action="store_true")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    docs = collect()
    if not args.no_combined:
        docs = docs + [combined(docs, "chemistry"), combined(docs, "physics")]
    if args.only:
        docs = [d for d in docs if d["key"] == args.only]
        if not docs:
            raise SystemExit(f"no document with key {args.only!r}")

    written = build(docs)
    if not args.only:
        write_index(docs, written)
    total = sum(p.stat().st_size for p in written)
    print(f"\nwrote {len(written)} PDFs, {total/1024/1024:.1f} MB total, under {OUT}")


if __name__ == "__main__":
    main()
