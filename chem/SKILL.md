# Chemistry notes from Sourabh Raina's videos — build spec

Read this whole file before building any artifact. It does not change between videos. If
anything here conflicts with your own judgement, follow this file — it was written and approved
by the user for exactly this purpose.

## Who this is for

Class XII CBSE student, DPS Indore. Half-yearly Chemistry paper: **10 September 2026**, 70
marks, 33 questions (16 one-markers [12 MCQ + 4 assertion-reason], 5 two-markers, 7
three-markers, 2 case studies of 4 marks, 3 long answers of 5 marks). Internal choice in one
2-mark, one 3-mark, and all three 5-mark questions.

Blueprint weights — see `chem/maps.json` → `exam.blueprint_weights` for the machine-readable
version:

| Ch | Chapter | Marks |
|----|---------|-------|
| 1 | Solutions | 15 |
| 2 | Electrochemistry | 14 |
| 3 | Chemical Kinetics | 13 |
| 4 | d and f Block Elements | 11 |
| 5 | Coordination Compounds | 11 |
| 6 | Haloalkanes and Haloarenes | 6 (full chapter, 6.1–6.8) |

Where the user stands: Chapters 1–3 are done at theory level — the gap there is **numericals**,
not concepts. Chapters 4–6 are **untouched — first contact.** Write those as teaching, not
revision.

## There are 12 videos, one artifact each

6 PYQ (past-year-question) videos and 6 one-shot lectures, one of each type per chapter. Video
IDs, NCERT file IDs, titles and favicons are all in `chem/maps.json` — copy from there, never
guess or re-derive.

## Rule 1 — prior-knowledge depth (the most important rule in this file)

The user was once handed a technically-correct Coordination Compounds summary written in
revision style and it "read as gibberish, because revision notes assume prior learning I didn't
have." Guard against exactly that, every time.

Before writing any line, apply this test: **could a student who has never heard this word follow
this sentence?**

- **Chapters 4, 5, 6** (d and f Block, Coordination Compounds, Haloalkanes) — assume the answer
  is NO for every technical term. Tag it `<span class="exposure-tag">exposure</span>` and give it
  **4–6 lines**: (1) what it is in plain words, (2) why it exists / what problem it solves, (3)
  one concrete example with real formulae or real numbers.
- **Chapters 1, 2, 3** (Solutions, Electrochemistry, Kinetics) — the student already knows the
  theory. Do **not** use the exposure tag. Teach the concept properly but keep the statement
  tight; put the length into **numerical method**, which is the actual gap.

Never put the exposure tag on Ch 1–3 material. `chem/qa.py` checks this mechanically — it fails
the build if a Ch1–3 file contains an exposure tag, or if a Ch4–6 file contains none.

## Rule 2 — PYQ artifact structure (exactly four parts, in this order, never reordered)

A past-questions video is not a chapter. Do not format it like one.

1. **Question types**, ranked by how often they appear. Per type: one-line recognition cue →
   numbered method steps → **the trap**.
2. **Mark slots** — which slot each type belongs to (1-marker / 2 / 3 / 4-mark case study / one
   of the three 5-markers). Take it from what the video states; if the video doesn't state marks,
   infer from question shape and write `(inferred)`.
3. **Repeat offenders** — questions or near-identical variants that appeared more than once
   across years. These are the highest-probability items in the whole chapter and the reason the
   video is worth watching. Give them their own visually distinct section (the `--repeat` color
   token, reserved for this section only).
4. **Numerical types** — **exactly one** fully worked example per type, then **three or four**
   more questions with answers only, no working. One model per pattern, then the student goes
   cold. Do not work every question.

Refer to questions as **year + number** (`2023 Q17`, `2019 Q5(b)`). Never reprint long question
text — one line of paraphrase, maximum.

## Rule 3 — one-shot artifact structure

Follow the chapter's own teaching order, as Sourabh sir gives it in the transcript. Per topic:
concept (depth per Rule 1) → the formula or reaction (KaTeX/mhchem) → one worked example if the
topic is numerical → what the examiner asks from this topic. Close with a final section
collecting every numerical pattern in the chapter in one place (heaviest for Ch 1–3, per the
numericals-gap note above).

## Rule 4 — style

- Short sentences. Plain words. If a line takes two reads to parse, rewrite it.
- No jargon unless NCERT or Xam Idea uses that exact term. If unavoidable, define it inline in
  five words, once, and move on.
- No introductions. Never write "in this video we will...". No summary of the summary.
- Never reprint the syllabus back at the reader.

## Rule 5 — chemistry rendering

- **Chemical equations/formulae → mhchem**: `$\ce{2H2 + O2 -> 2H2O}$`,
  `$\ce{[Co(NH3)6]^3+}$`. Handles subscripts, charges, arrows, states correctly.
- **Maths → plain KaTeX**: Nernst equation, Arrhenius equation, `$\Delta T_f = K_f \cdot m$`,
  rate laws, etc.
- Script order is non-negotiable: `katex.min.js` → `mhchem.min.js` → `auto-render.min.js` → the
  `renderMathInElement` call. `chem/template.html` already has this wired correctly — do not
  reorder the three `<script src=...>` tags.
- Delimiters: `$$…$$` for display, `$…$` for inline. `throwOnError: false`.
- `renderMathInElement` is scoped to `#chem-content`, never `document.body`. Do not change the
  target id unless you also change the `id="chem-content"` on `<main>` to match.

## Rule 6 — NCERT cross-check: when and how

Check against NCERT when: a term's spelling or definition matters, a formula or constant is
being stated, an IUPAC name is given, or the transcript sounds garbled.

1. Call `mcp__Google_Drive__read_file_content` with the chapter's `ncert_fileId` from
   `chem/maps.json`.
2. A full chapter (~60k chars) will exceed the tool's token cap — the error/result text names a
   local file path where the full text was saved. Use that path.
3. `grep` that saved file for distinctive surrounding words, not exact section-number strings —
   the extraction has drop-cap duplication artifacts (e.g. `5.15.15.1 Werner's Theory Theory
   Theory`) and section numbers that collide with worked-example/exercise numbers.
4. **NCERT is authoritative for**: term spelling, definitions, IUPAC names, standard formulae,
   constants, section numbering.
5. **NCERT is NOT the source for**: teaching order, exam technique, or question selection.
   Sourabh sir's material governs those — it is "the material," NCERT is only "for checks."
6. Equations *inside the extracted NCERT text* are unreliable (PDF extraction artifact). For any
   canonical formula, write the standard correct form yourself — do not copy a formula from the
   extracted text.

`chem/maps.json` → `ncert_read_procedure` restates this as a numbered list; `chem/maps.json` →
`chapters[].ncert_fileId` has every file ID you need.

## Rule 7 — transcript defect handling (there are no board frames here — no safety net but NCERT)

- **Garbled technical term** (auto-captions mangle Hinglish chemistry badly — e.g. "lanthanoid
  contraction" → "lantern node contraction"): correct it via NCERT (Rule 6). Never let a garbled
  term reach the notes.
- **Repeated block**: caption loops happen. Repetition is not emphasis — write the content once.
- **Transcript ends mid-topic**: say so in the artifact at the cutoff point, and tell the user in
  your reply.
- **Suspiciously short transcript** for a one-shot chapter: flag it and ask the user before
  writing anything.
- **Transcript content doesn't match the claimed chapter**: stop. Confirm with the user rather
  than producing a whole wrong artifact.
- **A number you cannot verify**: write it with a short "(verify)" marker rather than guessing.

## Rule 8 — design system (identical across all 12 artifacts, do not deviate)

`chem/template.html` already implements this. If you're filling it in, you inherit it for free —
do not edit the `<style>` blocks. If you ever rebuild from scratch, reproduce exactly:

- Phone-first, single column, ~62ch measure, `<summary>` tap targets ≥44px tall.
- Every top-level section is `<details>` (`<section class="block">` in the template) **closed by
  default**. `<summary>` = section/topic name + a short "what's inside" sub-line.
- Three-block theming cascade — a token defined only inside a media/data-theme block is the
  classic unreadable-artifact bug:
  - bare `:root { }` — full light palette
  - `@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { } }` — auto-dark
  - `:root[data-theme="dark"] { }` — explicit override (same dark values, duplicated)
  - `body` sets `background` from a token.
- Tokens (already in the template — do not change): light `--bg #F6F8F7 · --surface #FFFFFF ·
  --surface-alt #E9EEEC · --text #17211D · --text-muted #55635C · --border #D3DBD7 · --accent
  #1F6F5C · --accent-soft #D8EAE3 · --trap #A05A1E · --trap-soft #F6E9DA · --repeat #8C2F4A ·
  --repeat-soft #F7E1E7`; dark `--bg #101614 · --surface #182220 · --surface-alt #1F2B28 · --text
  #E6EDEA · --text-muted #97A6A0 · --border #2B3936 · --accent #5FBFA3 · --accent-soft #1E3A33 ·
  --trap #D9A05B · --trap-soft #35291B · --repeat #E58AA3 · --repeat-soft #3A2029`.
- Type: IBM Plex Sans 600/700 (headings/UI) · Public Sans 400/500 (body) · IBM Plex Mono 400/500
  (year-question refs, mark-slot badges, data). One Google Fonts `<link>`, real fallback stacks.
  All already wired in the template.
- `--trap` styles the trap callouts (`.trap`). `--repeat` is reserved for the Repeat Offenders
  section only (`.repeat-item`), so the highest-value content is visually unmistakable.
- Load the `artifact-design` skill before writing the first artifact of a session.

## Per-video execution checklist

1. Identify the video from `chem/maps.json` (chapter + type: `pyq_video_id` or
   `oneshot_video_id`). Confirm the pasted transcript's actual content matches that chapter
   before writing anything (Rule 7).
2. Save the transcript to `chem/transcripts/ch<N>-<pyq|oneshot>.txt`. Strip timestamps.
3. Skim for defects from Rule 7 first, before drafting.
4. Pull the chapter's NCERT text per Rule 6. Keep the saved grep-source path handy for
   spot-checks while writing.
5. Draft content per Rule 2 (PYQ) or Rule 3 (one-shot), applying Rule 1 depth throughout.
6. Copy `chem/template.html` to `chem/build/ch<N>-<pyq|oneshot>.html`. Fill in every
   `{{PLACEHOLDER}}`. Delete whichever of STRUCTURE A / STRUCTURE B you are not using (the
   template marks both with clear HTML comments — remove the unused block and its comments
   entirely). Fill `{{ARTIFACT_TITLE}}`, `{{CHAPTER_NUMBER}}`, `{{CHAPTER_NAME}}`,
   `{{VIDEO_TYPE_LABEL}}` (`"PYQ Patterns"` or `"One Shot"`) from `chem/maps.json`.
7. Run `python3 chem/qa.py chem/build/ch<N>-<pyq|oneshot>.html`. Fix every `FAIL` before
   publishing — do not publish with any check failing.
8. Publish via the Artifact tool with the exact `title` and `favicon` from `chem/maps.json`
   (`oneshot_title`/`pyq_title`, `oneshot_favicon`/`pyq_favicon`). Give the user the link.

`chem/qa.py` scripts most of this mechanically (see its own checks), but it cannot check content
quality — Rule 1 depth, Rule 2/3 structure content, Rule 4 style, Rule 7 defect handling are your
judgement calls, applied per this file.

## Verification once per artifact (things `chem/qa.py` cannot check)

- On the **published** page (not the local file — `file://` cannot reach cdnjs), confirm KaTeX
  and mhchem actually render: at least one `\ce{}` equation and one display formula.
- Toggle light/dark and confirm both are legible, including formula glyph colour.
- Spot-check one NCERT-verified term against the grep result you kept from step 4.

## Pilot note

The first artifact built should be Chapter 4, 5, or 6 (first-contact material), not Chapter 1 —
depth calibration (Rule 1) is the real risk on this job and it only shows up on first-contact
content. After the pilot is published, the user reads it on a phone and confirms the exposure
depth is right before the remaining 11 videos are built. Once signed off, the template and this
file are frozen — reuse unchanged for the rest.

## Where things live

```
chem/
  SKILL.md          # this file — read first, every time
  template.html     # artifact skeleton: KaTeX CSS inlined, both content structures, both scripts
  maps.json          # video IDs, NCERT file IDs, titles, favicons, exam blueprint -- copy from here
  qa.py             # python3 chem/qa.py chem/build/*.html -- run before every publish
  transcripts/      # pasted transcripts, one per video          [gitignored]
  build/            # generated HTML before publishing            [gitignored]
```
