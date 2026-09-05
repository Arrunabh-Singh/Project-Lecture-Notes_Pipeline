"""Convert every artifact this project produced into Markdown.

The pages were hand-authored, so this is not a general HTML-to-Markdown
converter -- it knows the specific component classes used by
chem/template.html, sheets/template.html and the earlier physics one-off
pages, and maps each to the Markdown that carries the same information:

    details.ch / section.block   ->  ## chapter or section heading
    details.f                    ->  ### <id> - <cue>, formula revealed inline
    div.deriv / .deriv-head      ->  ### <id> - <title>
    div.eq / div.result          ->  display maths on its own line
    table.syms / table.plain     ->  pipe table
    div.use / div.trap / .shared ->  labelled blockquote
    ol.steps + span.why          ->  numbered list, reason in italics
    figure.fig                   ->  **Figure.** <svg aria-label> + figcaption
    .qtype / .repeat-item /
    .cold-q / .exposure-tag      ->  the PYQ and first-contact components

KaTeX ($...$, $$...$$) and mhchem (\\ce{...}) are passed through untouched:
they are already the standard way to write maths in Markdown, and every
common renderer (GitHub, Obsidian, Typora, pandoc) understands them.

SVG figures cannot render inside a .md file, so each one becomes its
aria-label -- which was written as a full prose description of the figure
precisely so that it stands on its own here.

Two outputs, from one pass:

  markdown/          one .md per source page, for reading a topic at a time
  MASTER-NOTES.md    all of it concatenated, with a manifest and a table of
                     contents, for handing to another agent in one piece

Usage:
    python3 tools/export_markdown.py
    python3 tools/export_markdown.py --zip        # also bundles markdown.zip
"""
from __future__ import annotations

import argparse
import re
import shutil
import zipfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "markdown"
MASTER = ROOT / "MASTER-NOTES.md"

# ---------------------------------------------------------------- inline

INLINE_OPEN = {"b": "**", "strong": "**", "i": "*", "em": "*", "code": "`"}

# Tags that begin a new block. Any loose text sitting in the buffer when one
# of these opens belongs to what came *before* it, not to it -- the chapter
# pages write display maths as a bare $$...$$ text node between elements, and
# without this flush it gets swallowed into the following heading.
BLOCK_STARTS = {
    "p", "div", "table", "ul", "ol", "dl", "section", "details", "summary",
    "figure", "figcaption", "blockquote", "header", "footer", "hr",
    "h1", "h2", "h3", "h4", "h5", "h6",
}

# span classes that read as a monospace identifier
ID_SPANS = {"m-id", "fid", "d-num", "rx-id", "num"}
# span classes that read as a quieter trailing gloss
TAIL_SPANS = {"sub", "tail", "d-marks", "marks-badge", "m-count", "yr", "marks", "t-note"}


class Converter(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.buf: list[str] = []
        self.skip_depth = 0          # inside <svg>/<script>/<style>
        self.drop_depth = 0          # inside a badge whose text we replace
        self.stack: list[tuple[str, str]] = []   # (tag, class)
        self.table: list[list[str]] | None = None
        self.row: list[str] | None = None
        self.in_cell = False
        self.list_stack: list[str] = []   # "ol"/"ul"
        self.li_index: list[int] = []
        self.pending_fig: str | None = None
        self.callout = 0          # depth inside a use/trap/shared block

    # -- helpers -------------------------------------------------------
    def cls(self, attrs) -> str:
        return dict(attrs).get("class", "") or ""

    def flush(self, prefix: str = "") -> None:
        text = "".join(self.buf).strip()
        self.buf.clear()
        if text:
            self.out.append(prefix + re.sub(r"[ \t]+", " ", text))
            self.out.append("")

    def emit(self, line: str) -> None:
        self.out.append(line)
        self.out.append("")

    def close_italic(self) -> None:
        for i in range(len(self.out) - 1, -1, -1):
            if self.out[i].startswith("*"):
                self.out[i] = self.out[i] + "*"
                return

    # -- tags ----------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        c = self.cls(attrs)
        if tag in ("svg", "script", "style", "button"):
            # <button> is page furniture -- "Open all" / "Close all" toggles
            # mean nothing in a file that has no disclosure widgets.
            if tag == "svg":
                self.pending_fig = dict(attrs).get("aria-label")
            self.skip_depth += 1
            return
        if self.skip_depth:
            return

        # A block is opening: anything loose in the buffer is its own paragraph.
        if tag in BLOCK_STARTS and not self.in_cell:
            self.flush()

        self.stack.append((tag, c))

        if tag in INLINE_OPEN:
            self.buf.append(INLINE_OPEN[tag])
        elif tag == "sub":
            self.buf.append("_")
        elif tag == "sup":
            self.buf.append("^")
        elif tag == "a":
            if "rx-row" in c:
                self.flush()
            else:
                self.buf.append("[")
        elif tag == "br":
            self.buf.append("  \n")
        elif tag == "table":
            self.table = []
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.in_cell = True
            self.buf.clear()
        elif tag in ("ol", "ul"):
            self.list_stack.append(tag)
            self.li_index.append(0)
        elif tag == "li":
            self.buf.clear()
        elif tag == "span" and "why" in c:
            self.buf.append(" — *")
        elif tag == "span" and "exposure-tag" in c:
            # The badge's own text is the word "exposure"; the marker replaces
            # it rather than being printed alongside it.
            self.buf.append("**[exposure]** ")
            self.drop_depth += 1
        elif tag == "span" and ("lbl" in c or "worked-label" in c):
            self.buf.append("**")
        elif tag == "span" and c.startswith("dot"):
            pass
        elif tag == "span" and c in ID_SPANS:
            self.buf.append(" `")
        elif tag == "span" and c in TAIL_SPANS:
            self.buf.append(" — *")
        elif tag == "span" and "cut" in c:
            # the scope-warning line under a masthead: its own paragraph
            self.flush()
        elif tag == "div" and ("trap" in c or "use" in c or "shared" in c or "check" in c):
            self.callout += 1

    def handle_endtag(self, tag):
        if tag in ("svg", "script", "style", "button"):
            self.skip_depth = max(0, self.skip_depth - 1)
            if tag == "svg" and self.pending_fig:
                self.emit(f"**Figure.** {self.pending_fig}")
                self.pending_fig = None
            return
        if self.skip_depth:
            return
        c = ""
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                c = self.stack.pop(i)[1]
                break

        if tag in INLINE_OPEN:
            self.buf.append(INLINE_OPEN[tag])
        elif tag in ("sub", "sup"):
            pass
        elif tag == "a":
            if "rx-row" in c:
                self.flush("- ")
            else:
                self.buf.append("]")
        elif tag == "span" and "why" in c:
            self.buf.append("*")
        elif tag == "span" and "exposure-tag" in c:
            self.drop_depth = max(0, self.drop_depth - 1)
        elif tag == "span" and ("lbl" in c or "worked-label" in c):
            self.buf.append(":** ")
        elif tag == "span" and c in ID_SPANS:
            self.buf.append("` ")
        elif tag == "span" and c in TAIL_SPANS:
            self.buf.append("*")
        elif tag == "span" and "cut" in c:
            self.flush("*")
            self.close_italic()
        elif tag in ("td", "th"):
            self.in_cell = False
            if self.row is not None:
                self.row.append("".join(self.buf).strip().replace("|", "\\|"))
            self.buf.clear()
        elif tag == "tr":
            if self.table is not None and self.row:
                self.table.append(self.row)
            self.row = None
        elif tag == "table":
            self.write_table()
        elif tag in ("ol", "ul"):
            if self.list_stack:
                self.list_stack.pop()
                self.li_index.pop()
            self.out.append("")
        elif tag == "li":
            text = "".join(self.buf).strip()
            self.buf.clear()
            if text:
                if self.list_stack and self.list_stack[-1] == "ol":
                    self.li_index[-1] += 1
                    self.out.append(f"{self.li_index[-1]}. {text}")
                else:
                    self.out.append(f"- {text}")
        elif tag == "summary":
            enclosing = ""
            for t, cc in reversed(self.stack):
                if t == "details":
                    enclosing = cc
                    break
            self.flush("### " if "f" == enclosing.strip() else "## ")
        elif tag == "h1":
            self.flush("# ")
        elif tag in ("h2", "h3"):
            self.flush("### ")
        elif tag in ("h4", "h5", "h6"):
            self.flush("#### ")
        elif tag == "figcaption":
            self.flush("*")
            self.close_italic()
        elif tag == "p":
            c_low = c or ""
            if "setup" in c_low or "recognize" in c_low or "note" in c_low or "lede" in c_low or "standfirst" in c_low:
                self.flush("> " if "setup" in c_low else "*")
                if "setup" not in c_low:
                    self.close_italic()
            elif "eyebrow" in c_low:
                self.flush("`")
                for i in range(len(self.out) - 1, -1, -1):
                    if self.out[i].startswith("`"):
                        self.out[i] = self.out[i] + "`"
                        break
            elif self.callout:
                self.flush("> ")
            else:
                self.flush()
        elif tag == "div":
            if c in ("eq", "result"):
                text = "".join(self.buf).strip()
                self.buf.clear()
                if text:
                    self.emit(text)
            elif "trap" in c or "use" in c or "shared" in c or "check" in c:
                self.flush("> ")
                self.callout = max(0, self.callout - 1)
            elif "recog" in c:
                self.flush("> ")
            elif "deriv-head" in c or "tier-head" in c:
                self.flush("### ")
            elif "ty-name" in c:
                self.flush("**")
                for i in range(len(self.out) - 1, -1, -1):
                    if self.out[i].startswith("**"):
                        self.out[i] = self.out[i] + "**"
                        break
            elif "cold-q" in c:
                self.flush("- ")
            else:
                self.flush()
        elif tag in ("dt",):
            self.buf.append(": ")
        elif tag == "dd":
            self.flush("- ")
        elif tag in ("section", "details", "header", "footer", "figure"):
            self.flush()

    def handle_data(self, data):
        if self.skip_depth or self.drop_depth:
            return
        if data.strip() or (self.buf and not self.buf[-1].endswith(" ")):
            self.buf.append(data)

    def write_table(self):
        rows = self.table or []
        self.table = None
        if not rows:
            return
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        self.out.append("| " + " | ".join(rows[0]) + " |")
        self.out.append("|" + "---|" * width)
        for r in rows[1:]:
            self.out.append("| " + " | ".join(r) + " |")
        self.out.append("")

    def result(self) -> str:
        self.flush()
        text = "\n".join(self.out)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        return text.strip() + "\n"


def convert(html_text: str) -> str:
    # Drop authoring comments and the inlined stylesheets before parsing.
    html_text = re.sub(r"<!--.*?-->", "", html_text, flags=re.DOTALL)
    html_text = re.sub(r"<style.*?</style>", "", html_text, flags=re.DOTALL | re.IGNORECASE)
    html_text = re.sub(r"<script.*?</script>", "", html_text, flags=re.DOTALL | re.IGNORECASE)
    html_text = re.sub(r"<link[^>]*>", "", html_text, flags=re.IGNORECASE)
    c = Converter()
    c.feed(html_text)
    return c.result()


def chem_chapter_body(built_page: str) -> str:
    """Pull <main id="chem-content"> out of a fully built chapter page.

    Reading the built page rather than a scratch content fragment is what
    makes this export reproducible from a clean clone.
    """
    start = built_page.find('<main id="chem-content">')
    if start < 0:
        raise ValueError("no <main id=\"chem-content\"> in page")
    end = built_page.rfind("</main>")
    return built_page[start:end]


# ---------------------------------------------------------------- driver

CHEM_CHAPTERS = [
    ("ch1", "01-solutions", "Chapter 1 · Solutions"),
    ("ch2", "02-electrochemistry", "Chapter 2 · Electrochemistry"),
    ("ch3", "03-chemical-kinetics", "Chapter 3 · Chemical Kinetics"),
    ("ch4", "04-d-and-f-block", "Chapter 4 · The d- and f-Block Elements"),
    ("ch5", "05-coordination-compounds", "Chapter 5 · Coordination Compounds"),
    ("ch6", "06-haloalkanes-and-haloarenes", "Chapter 6 · Haloalkanes and Haloarenes"),
]

SHEETS = {
    "chem-formulas": ("chemistry", "every-chemistry-formula"),
    "chem-derivations": ("chemistry", "chemistry-derived"),
    "phys-formulas": ("physics", "every-physics-formula"),
    "phys-derivations": ("physics", "physics-derived"),
}

PHYS_CHAPTERS = {
    "leph101": "Chapter 1 · Electric Charges and Fields",
    "leph102": "Chapter 2 · Electrostatic Potential and Capacitance",
    "leph103": "Chapter 3 · Current Electricity",
    "leph104": "Chapter 4 · Moving Charges and Magnetism",
    "leph105": "Chapter 5 · Magnetism and Matter",
    "leph106": "Chapter 6 · Electromagnetic Induction",
    "leph107": "Chapter 7 · Alternating Current",
    "leph108": "Chapter 8 · Electromagnetic Waves",
}

# Pages that exist only as published artifacts; kept in the repo as Markdown
# so the master file can be rebuilt without going back to claude.ai.
PHYS_PAGES = [
    ("ray-optics-to-9-4.md", "Ray Optics to 9.4"),
    ("alternating-current-in-eight-derivations.md", "Alternating Current in Eight Derivations"),
    ("electromagnetic-waves-for-six-marks.md", "Electromagnetic Waves for Six Marks"),
]


# ------------------------------------------------------- master assembly

def rebase(md: str, base: int) -> str:
    """Shift every ATX heading so the document's own `#` sits at `base`."""
    delta = base - 1

    def shift(m: re.Match) -> str:
        level = min(6, len(m.group(1)) + delta)
        return "#" * level + " " + m.group(2)

    return re.sub(r"^(#{1,6}) +(.*)$", shift, md, flags=re.MULTILINE)


def strip_h1(md: str) -> str:
    """Drop a document's own title line; the master file supplies its own."""
    return re.sub(r"^# +.*$\n?", "", md, count=1, flags=re.MULTILINE).lstrip("\n")


def slug(text: str, seen: dict[str, int]) -> str:
    """GitHub-flavoured anchor slug, de-duplicated across the document."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]+", "", s, flags=re.UNICODE)   # drop punctuation
    s = s.replace(" ", "-")
    n = seen.get(s, 0)
    seen[s] = n + 1
    return s if n == 0 else f"{s}-{n}"


def build_toc(body: str) -> str:
    """A table of contents over the part (##) and document (###) headings."""
    seen: dict[str, int] = {}
    lines: list[str] = []
    for m in re.finditer(r"^(#{1,6}) +(.*)$", body, flags=re.MULTILINE):
        level, text = len(m.group(1)), m.group(2).strip()
        anchor = slug(text, seen)          # every heading consumes a slug
        if level == 2:
            lines.append(f"- [{text}](#{anchor})")
        elif level == 3:
            lines.append(f"    - [{text}](#{anchor})")
    return "\n".join(lines)


PREAMBLE = """# Class XII CBSE — Complete Notes: Physics and Chemistry

Everything built for one Class XII student at DPS Indore, in one file. It was
written from their own teacher's recorded lectures (transcribed, then
cross-checked against the board frames and the NCERT text), not from a
textbook summary, so the worked method is the point rather than the statement
of the result.

**The confirmed deadline is the chemistry half-yearly on 10 September 2026**,
70 marks, blueprint: Solutions 15 · Electrochemistry 14 · Chemical Kinetics 13
· d- and f-Block 11 · Coordination Compounds 11 · Haloalkanes 6. No physics
exam date has been given.

**Two depths, deliberately.** Chemistry chapters 1–3 are theory the student
already knows, so the length there goes into numerical method. Chapters 4–6 are
first contact: every technical term carries an **[exposure]** marker and is
defined in plain words with a concrete example before it is used again. The
physics notes are all board-grounded and flag any span the transcript could not
resolve confidently.

**Maths notation.** KaTeX throughout (`$...$` inline, `$$...$$` display), with
mhchem `\\ce{...}` for chemical formulae. The older physics one-off pages at the
end use plain-text maths instead — they predate the KaTeX pipeline.

**Figures.** The source pages carry drawn SVG diagrams. A `.md` file cannot show
them, so each appears here as **Figure.** followed by the full prose description
that was written as its accessible label — a description complete enough to
redraw from.

**Size.** This file is deliberately large. Read the manifest and contents below
and seek to the section you need rather than reading it top to bottom.
"""

MANIFEST = """## Manifest

| Section | Where it came from | What it is | Caveats |
|---|---|---|---|
| Chemistry chapters 1–6 | lecture transcripts + NCERT `lech101–105`, `lech201` | full chapter notes, exam-shaped, with past-year question sections | Ch4–6 carry `[exposure]` first-contact definitions; Ch1–3 assume the theory |
| Every Chemistry Formula | built across all six chapters | 50 entries, each with symbols, units, a recognition cue and its trap | 40 marked ● must-be-instant, 10 marked ○ |
| Chemistry, Derived | as above | 12 derivations, each ending in a formula that is on the formula sheet | figures are prose descriptions here |
| Every Physics Formula | the 57 chapter notes + NCERT `leph101–108` | 100 entries across chapters 1–9 | 78 marked ● must-be-instant, 22 marked ○; Ch9 rows come from the Ray Optics page, not from lectures |
| Physics, Derived | as above | 45 derivations, chapters 1–9, numbered PD1–PD45 | figures are prose descriptions here |
| Physics chapter notes 1–8 | 57 transcribed and verified lectures | the source of truth for every physics equation in this file | included verbatim; equations are board-grounded. **There is no Chapter 9 here** — those eighteen lectures have never been transcribed |
| Ray Optics to 9.4 | published page, no lecture source | Chapter 9 theory, four derivations, formula strip and question tiers | built for a test whose scope stopped at 9.4, so it skips lenses, prisms and instruments — those are in Physics, Derived instead |
| Alternating Current in Eight Derivations | published page | Chapter 7 in its own exam-shaped framing | eight derivations against the five (PD33–PD37) in Physics, Derived |
| Electromagnetic Waves for Six Marks | published page | Chapter 8, same shape | its five derivations include four that Physics, Derived does not carry — that book has one for Chapter 8 |

**Not included, and why.** Eight published physics chapter pages (one per
chapter, Ch1–8) exist as well. Their prose is a rendering of the same 57
chapter notes reproduced in full below, and their remaining bulk is embedded
board-frame photographs that cannot survive a Markdown export. Including them
would duplicate the largest block in this file for no added content.
"""

APPENDIX = """## Appendix — gaps, caveats and open questions

### Chapter 9 physics was never transcribed

Chapter 9 *is* covered here — seven derivations (PD39–PD45, including lenses,
the prism and both instruments) in **Physics, Derived**, twelve entries in
**Every Physics Formula**, and the whole **Ray Optics to 9.4** page. But all of
it was written from NCERT and from that earlier page, never from the teacher's
own lectures, so it carries the physics without the emphasis. There is no
`notes/leph109` to check it against.

Eighteen Ray Optics lecture videos (1.2 GB) sit in Google Drive folder
`1QC3JCSOfLxDxxZfW6rVxAIDAZs4Bkt0v`, and have never been transcribed. The
blocker is Google **Drive** OAuth, not the Gemini ASR key — that one is
configured and working. `DRIVE_CLIENT_ID`, `DRIVE_CLIENT_SECRET` and
`DRIVE_REFRESH_TOKEN` are all empty in `.env`; the access token in there
expired on 3 September. The folder is owned by the teacher rather than the
student, its anonymous download endpoint redirects to a login page, and the
MCP Drive connector caps downloads at 10 MB against files of 17–170 MB.

### A symbol clash still in the source

`notes/leph106` writes the solenoid self-inductance as `L = μ₀n²AL`, using `L`
for both the inductance and the length of the solenoid. Both sheets in this
file write it as `L = μ₀n²Al` and say so explicitly; the underlying note has
not been corrected.

### How much to trust the transcripts

Chemistry Chapter 6 had chunk-seam holes that passed the coverage, gap **and**
duplication checks at the same time — the segments on either side of a seam
overlapped in reported time while skipping real audio, so no automated check
could see the gap. About 36 lines (the SN2 mechanism, ambident nucleophiles,
organolithiums) and six past-year questions were recovered by re-transcribing
the audio windows directly. Anything similar elsewhere would be invisible to
the same checks, so read for sense, not just for coverage.

Where an equation extracted from the NCERT PDF disagrees with a board frame,
**the board frame is authoritative** — PDF flattening mangles the equations.

### Open question

No physics exam date has ever been given. The Ray Optics page was built for a
test that stopped at Section 9.4 and explicitly told the student to skip every
lens, prism and instrument question — advice that is wrong for any paper with a
wider scope, and the reason Physics, Derived covers lenses and instruments
while that page does not. If a physics paper is close, the scope needs
confirming before either is used for it.
"""


def write_index(written: list[Path]) -> None:
    """An index of the per-file export, regenerated with it."""
    lines = [
        "# Markdown export",
        "",
        "Every page this project produced, one Markdown file per source page.",
        "Generated by `tools/export_markdown.py` — edit the sources, not these files.",
        "",
        "For the same material as a **single** file (with a manifest, a table of",
        "contents and an appendix of known gaps), see `../MASTER-NOTES.md`.",
        "",
        "Maths is KaTeX (`$...$`, `$$...$$`) with mhchem `\\ce{...}`; the three physics",
        "one-off pages under `physics/pages/` use plain-text maths instead. SVG figures",
        "appear as **Figure.** followed by their full prose description.",
        "",
    ]
    groups: dict[str, list[Path]] = {}
    for path in written:
        rel = path.relative_to(OUT)
        groups.setdefault(str(rel.parent), []).append(rel)
    for parent in sorted(groups):
        lines.append(f"### `{parent}/`")
        lines.append("")
        for rel in sorted(groups[parent]):
            lines.append(f"- [{rel.name}]({rel.as_posix()})")
        lines.append("")
    (OUT / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", action="store_true", help="also write markdown.zip")
    args = ap.parse_args()

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "chemistry" / "chapters").mkdir(parents=True)
    (OUT / "physics" / "chapter-notes").mkdir(parents=True)
    (OUT / "physics" / "pages").mkdir(parents=True)

    written: list[Path] = []
    # (part, level-3 title, markdown) in the order they go into the master
    chem_parts: list[tuple[str, str]] = []
    phys_parts: list[tuple[str, str]] = []

    def emit_file(dest: Path, text: str) -> None:
        dest.write_text(text, encoding="utf-8")
        written.append(dest)

    # 1. the six chemistry chapter pages, read out of the built artifacts
    for key, stem, title in CHEM_CHAPTERS:
        src = ROOT / "chem" / "build" / f"{key}.html"
        if not src.exists():
            print(f"  skip {key}: {src} not found")
            continue
        md = convert(chem_chapter_body(src.read_text(encoding="utf-8")))
        emit_file(OUT / "chemistry" / "chapters" / f"{stem}.md", md)
        chem_parts.append((title, md))

    # 2. the four cross-chapter sheets
    sheet_md: dict[str, str] = {}
    for name, (subject, stem) in SHEETS.items():
        src = ROOT / "sheets" / "content" / f"{name}.html"
        if not src.exists():
            print(f"  skip {name}: {src} not found")
            continue
        md = convert(src.read_text(encoding="utf-8"))
        emit_file(OUT / subject / f"{stem}.md", md)
        sheet_md[name] = md

    for name, title in (("chem-formulas", "Every Chemistry Formula"),
                        ("chem-derivations", "Chemistry, Derived")):
        if name in sheet_md:
            chem_parts.append((title, sheet_md[name]))
    for name, title in (("phys-formulas", "Every Physics Formula"),
                        ("phys-derivations", "Physics, Derived")):
        if name in sheet_md:
            phys_parts.append((title, sheet_md[name]))

    # 3. the physics chapter notes, which are already Markdown
    notes_sections: list[tuple[str, str]] = []
    for chapter_dir in sorted((ROOT / "notes").glob("leph1*")):
        target = OUT / "physics" / "chapter-notes" / chapter_dir.name
        target.mkdir(parents=True, exist_ok=True)
        bodies: list[str] = []
        for md_path in sorted(chapter_dir.glob("*.md")):
            shutil.copy2(md_path, target / md_path.name)
            written.append(target / md_path.name)
            bodies.append(rebase(md_path.read_text(encoding="utf-8"), 4))
        if bodies:
            head = PHYS_CHAPTERS.get(chapter_dir.name, chapter_dir.name)
            notes_sections.append((f"{head} — lecture notes", "\n\n".join(bodies)))

    phys_parts.extend(notes_sections)

    # 4. the three physics pages that exist only as published artifacts
    for fname, title in PHYS_PAGES:
        src = ROOT / "notes" / "pages" / fname
        if not src.exists():
            print(f"  skip {fname}: {src} not found")
            continue
        md = src.read_text(encoding="utf-8")
        shutil.copy2(src, OUT / "physics" / "pages" / fname)
        written.append(OUT / "physics" / "pages" / fname)
        phys_parts.append((title, md))

    write_index(written)
    print(f"wrote {len(written)} markdown files under {OUT}")

    # 5. the master file
    body_parts: list[str] = []
    for part_title, sections in (("Part I — Chemistry", chem_parts),
                                 ("Part II — Physics", phys_parts)):
        body_parts.append(f"## {part_title}")
        for title, md in sections:
            if title.endswith("— lecture notes"):
                # already rebased per note; each note keeps its own title at ####
                body_parts.append(f"### {title}\n\n{md}")
            else:
                body_parts.append(f"### {title}\n\n{rebase(strip_h1(md), 3)}")
    body = "\n\n".join(body_parts) + "\n\n" + APPENDIX

    toc = build_toc(body)
    master = (
        PREAMBLE
        + "\n" + MANIFEST
        + "\n## Contents\n\n" + toc + "\n\n---\n\n"
        + body
    )
    master = re.sub(r"\n{3,}", "\n\n", master).strip() + "\n"
    MASTER.write_text(master, encoding="utf-8")
    print(f"wrote {MASTER} ({MASTER.stat().st_size/1024:.0f} KB)")

    if args.zip:
        bundle = ROOT / "markdown.zip"
        with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted(OUT.rglob("*.md")):
                z.write(p, p.relative_to(OUT.parent))
            z.write(MASTER, MASTER.name)
        print(f"bundled {bundle} ({bundle.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
