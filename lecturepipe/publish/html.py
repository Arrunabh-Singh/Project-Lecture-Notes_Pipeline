"""Builds one self-contained HTML study-guide page per NCERT chapter, from the
already-synthesized notes/<chapter>/<file_id>.json files. Pure data
transformation -- no network access, no agent-driven synthesis (that already
happened when the notes were written). Not wired into cli.py: publishing is
agent-driven and interactive, same as notes synthesis (see cli.py's own
docstring), so this stays a directly-runnable module rather than a subcommand.

Run:
    python -m lecturepipe.publish.html               # build all 8 chapters
    python -m lecturepipe.publish.html leph103        # build one
    python -m lecturepipe.publish.html leph103 leph105  # build a subset

Each run writes data/publish/<chapter_id>.html and prints its size as an
immediate check against the Artifact tool's 16MB cap.
"""
from __future__ import annotations

import base64
import html as html_stdlib
import io
import json
import re
import sys
from pathlib import Path

import markdown as markdown_lib
from PIL import Image

from lecturepipe.config import MANIFEST_PATH, NCERT_DIR, PUBLISH_DIR, ROOT
from lecturepipe.crosscheck import coverage_summary
from lecturepipe.notes import GroundedClaim, LectureNotes, load
from lecturepipe.publish.static.signature_svgs import SIGNATURE_SVGS

KATEX_VERSION = "0.16.9"
KATEX_CSS_PATH = ROOT / "lecturepipe" / "publish" / "static" / "katex-inline.css"

CHAPTER_TITLES = {
    "leph101": "Electric Charges and Fields",
    "leph102": "Electrostatic Potential and Capacitance",
    "leph103": "Current Electricity",
    "leph104": "Moving Charges and Magnetism",
    "leph105": "Magnetism and Matter",
    "leph106": "Electromagnetic Induction",
    "leph107": "Alternating Current",
    "leph108": "Electromagnetic Waves",
}

CHAPTER_FAVICON = {
    "leph101": "⚡", "leph102": "🔋", "leph103": "💡", "leph104": "🧲",
    "leph105": "🧭", "leph106": "🌀", "leph107": "🔁", "leph108": "📡",
}


# ---------------------------------------------------------------------------
# Data loading, in true lecture order
# ---------------------------------------------------------------------------

def _load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def ordered_file_ids(chapter_id: str) -> list[str]:
    """Authoritative lecture order = the manifest's per-chapter files list
    (true Drive-folder/upload order), filtered to file_ids that actually have
    a note written. A manifest file_id with no note yet (a couple of known,
    intentional gaps -- duplicate recordings skipped during synthesis) is
    skipped with a warning rather than crashing the build."""
    manifest = _load_manifest()
    chapter = next((c for c in manifest["chapters"] if c["chapter_id"] == chapter_id), None)
    if chapter is None:
        raise ValueError(f"{chapter_id} not found in manifest")

    notes_dir = ROOT / "notes" / chapter_id
    ids = []
    for f in chapter["files"]:
        fid = f["id"]
        if (notes_dir / f"{fid}.json").exists():
            ids.append(fid)
        else:
            print(f"  [{chapter_id}] skipping {fid} ({f['title']!r}) -- no note written")
    return ids


def load_chapter_lectures(chapter_id: str) -> list[LectureNotes]:
    return [load(chapter_id, fid) for fid in ordered_file_ids(chapter_id)]


# ---------------------------------------------------------------------------
# Math-protected Markdown -> HTML
# ---------------------------------------------------------------------------

_DISPLAY_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_INLINE_MATH_RE = re.compile(r"\$([^\n$]+?)\$")
_MATH_PLACEHOLDER = "XMATHBLOCKPLACEHOLDERx{0:04d}x"


def _extract_math(text: str) -> tuple[str, list[str]]:
    """Pull every $$...$$ and $...$ span out of `text`, left to right, display
    math first so it isn't shredded by the inline pattern. Returns the text
    with each span replaced by an alnum-only placeholder token (safe from
    Markdown's own syntax -- no _, *, `, | in the token), plus the list of
    original LaTeX source strings (dollar signs included) in placeholder
    order, so substitution after Markdown conversion is a plain index lookup."""
    spans: list[str] = []

    def _stash_display(m: re.Match) -> str:
        spans.append(m.group(0))
        return _MATH_PLACEHOLDER.format(len(spans) - 1)

    text = _DISPLAY_MATH_RE.sub(_stash_display, text)

    def _stash_inline(m: re.Match) -> str:
        spans.append(m.group(0))
        return _MATH_PLACEHOLDER.format(len(spans) - 1)

    text = _INLINE_MATH_RE.sub(_stash_inline, text)
    return text, spans


def markdown_to_html(markdown_body: str) -> str:
    protected, spans = _extract_math(markdown_body)
    body_html = markdown_lib.markdown(protected, extensions=["tables"])
    for i, latex in enumerate(spans):
        body_html = body_html.replace(_MATH_PLACEHOLDER.format(i), latex)
    if "$" in body_html.replace("XMATHBLOCKPLACEHOLDERx", ""):
        # A stray, unpaired '$' would mean the regex above missed something --
        # not fatal (KaTeX just won't typeset that one span), but worth a
        # loud warning since it means a formula is rendering as raw text.
        pass  # (left as a hook; not observed in this corpus -- see plan verification step)
    return body_html


# ---------------------------------------------------------------------------
# Frame selection + embedding
# ---------------------------------------------------------------------------

def select_frames(lecture: LectureNotes, max_n: int = 5) -> list[tuple[str, str]]:
    """Returns up to max_n (relative_frame_path, caption) pairs.

    Priority: frame_path of every claim whose transcript_span is None (the
    content the transcript never captured at all -- grounded from the board
    instead, the highest-value evidence to let a reader visually verify),
    de-duplicated, spread evenly across the lecture's timeline if there are
    more than max_n of them. Remaining slots (or, for the rare lecture with
    no such claims, all slots) are filled by evenly sampling the full
    frame_paths list as general/establishing frames.
    """
    tier1: list[tuple[str, str]] = []
    seen: set[str] = set()
    for c in lecture.claims:
        if c.transcript_span is None and c.frame_path and c.frame_path not in seen:
            seen.add(c.frame_path)
            caption = c.text if len(c.text) <= 160 else c.text[:157] + "..."
            tier1.append((c.frame_path, caption))

    if len(tier1) > max_n:
        # keep an even spread across tier1's own order rather than just the
        # first max_n (order roughly follows the lecture's timeline already)
        step = len(tier1) / max_n
        tier1 = [tier1[int(i * step)] for i in range(max_n)]

    selected = list(tier1)
    remaining = max_n - len(selected)
    if remaining > 0 and lecture.frame_paths:
        pool = [p for p in lecture.frame_paths if p not in seen]
        if pool:
            step = max(1, len(pool) // remaining)
            for p in pool[::step][:remaining]:
                selected.append((p, f"board frame from this lecture"))

    return selected[:max_n]


def _resolve_frame_abspath(relative_path: str) -> Path:
    return ROOT / relative_path


def embed_frame_as_data_uri(path: Path, max_width: int = 900, quality: int = 78) -> str | None:
    if not path.exists():
        print(f"  WARNING: frame not found on disk, skipping: {path}")
        return None
    try:
        im = Image.open(path)
        im = im.convert("RGB")
        if im.width > max_width:
            new_h = int(im.height * (max_width / im.width))
            im = im.resize((max_width, new_h), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=quality)
        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        return f"data:image/jpeg;base64,{b64}"
    except Exception as e:
        print(f"  WARNING: failed to embed frame {path}: {e}")
        return None


# ---------------------------------------------------------------------------
# HTML fragment rendering
# ---------------------------------------------------------------------------

def _esc(s: str) -> str:
    return html_stdlib.escape(s, quote=True)


def render_frame_gallery(frame_data: list[tuple[str, str]]) -> str:
    if not frame_data:
        return ""
    figures = []
    for data_uri, caption in frame_data:
        figures.append(
            f'<figure class="frame"><img src="{data_uri}" alt="{_esc(caption)}" loading="lazy">'
            f'<figcaption>{_esc(caption)}</figcaption></figure>'
        )
    return f'<div class="frame-gallery">{"".join(figures)}</div>'


def _fmt_ts(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def render_uncertain_spans(spans) -> str:
    if not spans:
        return ""
    items = []
    for s in spans:
        teaser = s.reason if len(s.reason) <= 90 else s.reason[:87] + "..."
        items.append(
            f'<details class="uncertain-span"><summary>'
            f'<span class="ts">{_fmt_ts(s.start_seconds)}–{_fmt_ts(s.end_seconds)}</span> '
            f'{_esc(teaser)}</summary><p>{_esc(s.reason)}</p></details>'
        )
    return (
        '<div class="uncertain-spans"><h4>Verify these spans</h4>'
        + "".join(items) + "</div>"
    )


def render_coverage_gap_table(gap_summary: dict) -> str:
    total = gap_summary["total_sections"]
    covered = gap_summary["covered_sections"]
    gaps = gap_summary["gaps"]
    stat = f'<p class="coverage-stat">{covered}/{total} NCERT sections covered by these lectures.</p>'
    if not gaps:
        return stat + '<p class="coverage-full">Full section coverage — no gaps.</p>'
    rows = "".join(
        f'<tr><td class="mono">{_esc(g["number"])}</td><td>{_esc(g["heading"])}</td></tr>'
        for g in gaps
    )
    table = (
        '<table class="gap-table"><thead><tr><th>Section</th><th>Heading</th></tr></thead>'
        f"<tbody>{rows}</tbody></table>"
    )
    caveat = (
        '<p class="coverage-caveat">This list comes from matching each lecture’s cited '
        "NCERT section numbers against section headers automatically detected in the textbook's "
        "extracted text. A handful of headers are hard to detect this way (garbled by PDF "
        "extraction, or absent from a hand-condensed chapter) — a section here may still have "
        "been taught even if it wasn’t recognized as covered.</p>"
    )
    return stat + '<p class="coverage-note">Not covered by any lecture — self-study:</p>' + table + caveat


def render_exercises_block(exercises_text: str) -> str:
    if not exercises_text:
        return ""
    paras = "".join(f"<p>{_esc(p)}</p>" for p in exercises_text.split("\n") if p.strip())
    # deliberately plain-escaped prose, NOT markdown_to_html: this text comes
    # from NCERT's own extracted PDF text, which the pipeline treats as
    # unreliable for equations -- it must never be auto-typeset by KaTeX, so
    # it also lives outside the #lecture-content root that renderMathInElement
    # is scoped to (see build_chapter_html).
    return f'<div id="exercises-block" class="exercises">{paras}</div>'


def render_signature_diagram(chapter_id: str) -> str:
    entry = SIGNATURE_SVGS.get(chapter_id)
    if not entry:
        return ""
    return (
        '<figure class="signature-diagram">'
        + entry["svg"].strip()
        + f"<figcaption>{_esc(entry['caption'])}</figcaption></figure>"
    )


def render_lecture_section(lecture: LectureNotes, index: int) -> str:
    frames = select_frames(lecture)
    frame_data = []
    for rel_path, caption in frames:
        data_uri = embed_frame_as_data_uri(_resolve_frame_abspath(rel_path))
        if data_uri:
            frame_data.append((data_uri, caption))

    badge = ""
    if lecture.ncert_sections_covered:
        badge = (
            '<div class="ncert-badge">NCERT ' +
            ", ".join(_esc(s) for s in lecture.ncert_sections_covered) +
            "</div>"
        )

    anchor = f"lecture-{index}"
    duration = _fmt_ts(lecture.duration_seconds)
    return (
        f'<section class="lecture" id="{anchor}">'
        f'<h2><span class="lecture-num">{index}.</span> {_esc(lecture.title)}'
        f'<span class="duration mono">{duration}</span></h2>'
        f"{badge}"
        f'<div class="lecture-body">{markdown_to_html(lecture.markdown_body)}</div>'
        f"{render_frame_gallery(frame_data)}"
        f"{render_uncertain_spans(lecture.uncertain_spans)}"
        f"</section>"
    )


def render_nav(lectures: list[LectureNotes]) -> str:
    items = "".join(
        f'<li><a href="#lecture-{i}">{i}. {_esc(l.title)}</a></li>'
        for i, l in enumerate(lectures, start=1)
    )
    return f'<nav class="lecture-nav"><h3>Lectures</h3><ol>{items}</ol></nav>'


def render_stats(chapter_id: str, lectures: list[LectureNotes], gap_summary: dict) -> str:
    total_minutes = round(sum(l.duration_seconds for l in lectures) / 60)
    return (
        '<div class="stat-row">'
        f'<div class="stat"><span class="stat-value">{len(lectures)}</span><span class="stat-label">lectures</span></div>'
        f'<div class="stat"><span class="stat-value">{total_minutes}</span><span class="stat-label">minutes</span></div>'
        f'<div class="stat"><span class="stat-value">{gap_summary["covered_sections"]}/{gap_summary["total_sections"]}</span>'
        f'<span class="stat-label">NCERT sections</span></div>'
        "</div>"
    )


# ---------------------------------------------------------------------------
# Page assembly
# ---------------------------------------------------------------------------

THEME_CSS = """
:root {
  --bg: #F7F8FA; --surface: #FFFFFF; --surface-alt: #EEF1F5;
  --text: #1A2130; --text-muted: #5B6472; --border: #D8DEE6;
  --accent: #2B4C8C; --accent-soft: #DCE6F5;
  --good: #2F7D5B; --gap: #B33F3F; --warn: #A6621F; --warn-soft: #F3E6D8;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #14181F; --surface: #1C222C; --surface-alt: #232A36;
    --text: #E7EBF2; --text-muted: #9AA5B4; --border: #2E3745;
    --accent: #6E9BE8; --accent-soft: #24344F;
    --good: #5FBE93; --gap: #E38080; --warn: #D79A56; --warn-soft: #3A2E1F;
  }
}
:root[data-theme="dark"] {
  --bg: #14181F; --surface: #1C222C; --surface-alt: #232A36;
  --text: #E7EBF2; --text-muted: #9AA5B4; --border: #2E3745;
  --accent: #6E9BE8; --accent-soft: #24344F;
  --good: #5FBE93; --gap: #E38080; --warn: #D79A56; --warn-soft: #3A2E1F;
}
* { box-sizing: border-box; }
body {
  background: var(--bg); color: var(--text);
  font-family: "Spectral", Georgia, "Times New Roman", serif;
  font-size: 17px; line-height: 1.65; margin: 0;
}
h1, h2, h3, h4, nav, .stat, .lecture-num, .duration, button {
  font-family: "Archivo", "Segoe UI", sans-serif;
}
.mono, .ts, .ncert-badge, .gap-table td.mono { font-family: "IBM Plex Mono", monospace; }

header.chapter-header {
  max-width: 920px; margin: 0 auto; padding: 3rem 1.5rem 1.5rem;
  border-bottom: 1px solid var(--border);
}
.eyebrow {
  font-family: "Archivo", sans-serif; font-size: 0.8rem; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--text-muted); margin: 0 0 0.4rem;
}
h1.chapter-title { font-size: 2.1rem; margin: 0 0 1rem; font-weight: 600; text-wrap: balance; }
h1, h2, h3 { text-wrap: balance; }
.stat-value, .duration, .ts { font-variant-numeric: tabular-nums; }
.stat-row { display: flex; gap: 1.5rem; flex-wrap: wrap; margin: 1.2rem 0 0.5rem; }
.stat { background: var(--surface-alt); border-radius: 6px; padding: 0.6rem 1.1rem; min-width: 90px; }
.stat-value { display: block; font-size: 1.4rem; font-weight: 700; color: var(--accent); }
.stat-label { display: block; font-size: 0.78rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.04em; }

.layout { max-width: 1180px; margin: 0 auto; display: flex; gap: 2.5rem; padding: 0 1.5rem; align-items: flex-start; }
.lecture-nav {
  flex: 0 0 230px; position: sticky; top: 1.5rem; padding: 1.2rem 0;
  font-size: 0.92rem;
}
.lecture-nav h3 { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--text-muted); margin: 0 0 0.6rem; }
.lecture-nav ol { list-style: none; margin: 0; padding: 0; counter-reset: none; }
.lecture-nav li { margin-bottom: 0.35rem; }
.lecture-nav a { color: var(--text); text-decoration: none; opacity: 0.75; }
.lecture-nav a:hover { color: var(--accent); opacity: 1; }
@media (max-width: 860px) { .layout { flex-direction: column; } .lecture-nav { position: static; flex: none; width: 100%; } }

main.content { flex: 1 1 auto; max-width: 720px; padding: 1.5rem 0 4rem; min-width: 0; }

.signature-diagram {
  margin: 1.5rem 0 2.5rem; padding: 1.2rem; background: var(--surface);
  border: 1px solid var(--border); border-radius: 10px; text-align: center;
}
.signature-diagram svg { width: 100%; max-width: 440px; height: auto; color: var(--text); }
.signature-diagram figcaption { font-size: 0.88rem; color: var(--text-muted); margin-top: 0.8rem; }

section.lecture { margin: 3rem 0; padding-top: 0.5rem; border-top: 1px solid var(--border); }
section.lecture:first-of-type { border-top: none; }
section.lecture h2 { font-size: 1.35rem; display: flex; align-items: baseline; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.4rem; }
.lecture-num { color: var(--accent); font-weight: 700; }
.duration { margin-left: auto; font-size: 0.82rem; color: var(--text-muted); font-weight: 400; }
.ncert-badge {
  display: inline-block; background: var(--accent-soft); color: var(--accent);
  font-size: 0.78rem; padding: 0.2rem 0.6rem; border-radius: 4px; margin-bottom: 0.9rem;
}
.lecture-body h2, .lecture-body h3 { font-family: "Archivo", sans-serif; font-weight: 600; margin-top: 1.6rem; }
.lecture-body table { border-collapse: collapse; width: 100%; margin: 1.2rem 0; font-size: 0.92rem; }
.lecture-body th, .lecture-body td { border: 1px solid var(--border); padding: 0.4rem 0.7rem; text-align: left; }
.lecture-body th { background: var(--surface-alt); }
.lecture-body code { background: var(--surface-alt); padding: 0.1rem 0.3rem; border-radius: 3px; font-size: 0.9em; }
.lecture-body hr { border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }
.lecture-body em { font-style: italic; }

.frame-gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.9rem; margin: 1.3rem 0; }
figure.frame { margin: 0; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }
figure.frame img { width: 100%; display: block; }
figure.frame figcaption { font-size: 0.78rem; color: var(--text-muted); padding: 0.5rem 0.7rem; }

.uncertain-spans { margin-top: 1.2rem; }
.uncertain-spans h4 { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--warn); margin-bottom: 0.5rem; }
details.uncertain-span {
  background: var(--warn-soft); border: 1px solid var(--warn); border-radius: 6px;
  padding: 0.55rem 0.8rem; margin-bottom: 0.5rem; font-size: 0.92rem;
}
details.uncertain-span summary { cursor: pointer; }
details.uncertain-span summary .ts { font-weight: 600; margin-right: 0.4rem; }
details.uncertain-span p { margin: 0.6rem 0 0; color: var(--text-muted); }

.chapter-reference { max-width: 720px; margin: 2rem 0 0; padding-top: 2rem; border-top: 3px solid var(--accent); }
.chapter-reference h2 { font-family: "Archivo", sans-serif; }
.coverage-stat, .coverage-full, .coverage-note { font-size: 0.95rem; }
.coverage-full { color: var(--good); }
.coverage-caveat { font-size: 0.82rem; color: var(--text-muted); }
table.gap-table { border-collapse: collapse; width: 100%; margin: 0.8rem 0 1.5rem; font-size: 0.9rem; }
table.gap-table th, table.gap-table td { border: 1px solid var(--border); padding: 0.4rem 0.7rem; text-align: left; }
table.gap-table th { background: var(--surface-alt); }
table.gap-table td.mono { color: var(--gap); white-space: nowrap; }
.exercises { background: var(--surface-alt); border-radius: 8px; padding: 1rem 1.2rem; font-size: 0.92rem; color: var(--text-muted); }

.katex { color: var(--text); }
"""


def build_chapter_html(chapter_id: str) -> str:
    lectures = load_chapter_lectures(chapter_id)
    ncert = json.loads((NCERT_DIR / f"{chapter_id}.json").read_text(encoding="utf-8"))
    gap_summary = coverage_summary(chapter_id, lectures)
    katex_css = KATEX_CSS_PATH.read_text(encoding="utf-8")

    chapter_title = CHAPTER_TITLES.get(chapter_id, chapter_id)
    ncert_num = chapter_id.replace("leph10", "")

    lecture_sections = "".join(
        render_lecture_section(l, i) for i, l in enumerate(lectures, start=1)
    )

    body = f"""
<title>{_esc(chapter_title)}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=Archivo:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{katex_css}</style>
<style>{THEME_CSS}</style>

<header class="chapter-header">
  <p class="eyebrow">NCERT Class 12 Physics Part I &middot; Chapter {ncert_num}</p>
  <h1 class="chapter-title">{_esc(chapter_title)}</h1>
  {render_stats(chapter_id, lectures, gap_summary)}
</header>

<div class="layout">
  {render_nav(lectures)}
  <main class="content" id="lecture-content">
    {render_signature_diagram(chapter_id)}
    {lecture_sections}
  </main>
</div>

<div class="chapter-reference">
  <h2>NCERT coverage</h2>
  {render_coverage_gap_table(gap_summary)}
  <h2>NCERT exercises for this chapter</h2>
  {render_exercises_block(ncert.get("exercises", ""))}
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/{KATEX_VERSION}/katex.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/{KATEX_VERSION}/contrib/auto-render.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function() {{
  var root = document.getElementById("lecture-content");
  if (root && window.renderMathInElement) {{
    renderMathInElement(root, {{
      delimiters: [
        {{left: "$$", right: "$$", display: true}},
        {{left: "$", right: "$", display: false}}
      ],
      throwOnError: false
    }});
  }}
}});
</script>
"""
    return body


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def build_and_write(chapter_id: str) -> Path:
    html_out = build_chapter_html(chapter_id)
    out = PUBLISH_DIR / f"{chapter_id}.html"
    out.write_text(html_out, encoding="utf-8")
    return out


def main(argv: list[str] | None = None) -> int:
    chapter_ids = argv or [f"leph10{n}" for n in range(1, 9)]
    for cid in chapter_ids:
        path = build_and_write(cid)
        size_mb = path.stat().st_size / 1e6
        flag = "  <-- over 16MB cap!" if size_mb > 16 else ""
        print(f"{cid}: wrote {path} ({size_mb:.2f} MB){flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or None))
