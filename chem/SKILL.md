# Chemistry notes from Sourabh Raina's videos

Read this whole file before touching any transcript. It is the spec, not a summary of one —
follow it literally.

## Who this is for

Class XII CBSE student (DPS Indore). Half-yearly Chemistry paper: **10 September 2026**, 70
marks, 33 questions (16 one-markers [12 MCQ + 4 assertion-reason], 5 two-markers, 7
three-markers, 2 case studies of 4 marks, 3 long answers of 5 marks). Internal choice in one
2-mark, one 3-mark, and all three 5-mark questions.

Blueprint weights — every mark is accounted for, sums to 70:

| Ch | Name | Marks |
|----|------|-------|
| 1 | Solutions | 15 |
| 2 | Electrochemistry | 14 |
| 3 | Chemical Kinetics | 13 |
| 4 | d and f Block Elements | 11 |
| 5 | Coordination Compounds | 11 |
| 6 | Haloalkanes and Haloarenes | 6 (full chapter, 6.1–6.8 — not limited to 6.1–6.2) |

Chapters 1–3 are theory-known; the user's gap there is numericals. Chapters 4–6 are **first
contact** — the user has never studied this material before.

## The deliverable — read this before writing anything

**One published Artifact per chapter (6 total, not 12).** Each chapter's artifact contains its
lecture (one-shot) notes first, then that chapter's numerical-patterns-collected closer, then
its PYQ (past-year-questions) section, appended last. The two halves usually arrive as separate
pasted transcripts, in either order, possibly in different sessions — see §3a for exactly how to
build and update the combined page across two passes.

Never treat a video as an artifact by itself. A video is one half of a chapter's artifact.

## Settled facts — do not re-investigate

- **YouTube fetching is blocked in this environment**, confirmed three independent ways: yt-dlp
  captions (HTTP 429, "Sign in to confirm you're not a bot"), yt-dlp audio-only extraction (same
  error, at the same webpage-extraction step every request type shares), and
  `youtube-transcript-api` (explicit `IpBlocked` error — this container's outbound IP is a
  cloud-provider range YouTube blocks outright). Do not re-attempt any of these, and do not try
  cookie exports or proxy workarounds — that's circumventing anti-bot measures, not a bug to
  route around.
- **Fallback: the user downloads audio on their own (unblocked) machine and uploads it to
  Google Drive; this session pulls it from Drive and runs it through Gemini ASR.** See
  `chem/transcribe.py` — reuses `lecturepipe/asr/gemini.py` and `lecturepipe/asr/verify.py`
  as-is (same Files API upload, 429/503 retry, fabricated-tail sanitize) with `subject`
  generalized so the prompt says "Chemistry" instead of being hardcoded to physics. That script
  takes a LOCAL file path only — pull the file down from Drive first via the
  `mcp__Google_Drive__*` tools, then run the script. Output is raw ASR text: still run it
  through §7 defect handling exactly like a pasted transcript before drafting notes from it. If
  the user pastes a transcript directly, skip this whole path — it's a fallback, not the
  default.
- **NCERT is the only independent correctness check** (no board-frame safety net here, unlike
  the physics project this pipeline was built from).
- **NCERT is reachable** via the Google Drive connector
  (`mcp__Google_Drive__read_file_content`). A full chapter read is ~60k chars, **exceeds the
  tool's token cap, and auto-saves to a local file** — the tool's error/result text names the
  path. Read that path with `grep`, not the MCP tool again.
- Extracted NCERT text has PDF artifacts: drop-cap runs (e.g. "5.15.15.1 Werner's Theory Theory
  Theory"), section numbers colliding with worked-example/exercise numbers. Grep on distinctive
  surrounding words, not exact section-number strings.
- Equations inside the extracted NCERT *text* are unreliable — same PDF-extraction problem as
  the physics project. For any formula, write the canonical correct form yourself; don't copy
  one out of the extracted text.
- **KaTeX assets are ready to use as-is** — `chem/template.html` already has the full KaTeX CSS
  inlined (spliced from `lecturepipe/publish/static/katex-inline.css`) and the three required
  `<script>` tags at the bottom, in the required order. Never touch that part of the template.
- **mhchem** (`\ce{...}`) handles chemical equations/formulae — subscripts, charges, arrows,
  states. Use it for every chemical equation and formula. Use plain KaTeX (`$...$` / `$$...$$`)
  for ordinary maths (Nernst, Arrhenius, rate laws, `\Delta T_f = K_f \cdot m`, etc).
- Never paste raw transcript sentences into the artifact as a stand-in for writing the note. The
  content must be original teaching prose grounded in the transcript, not a copy of it — both
  because a copy-paste note is exactly the "revision style, unreadable to a first-time reader"
  failure this job exists to avoid, and because reproducing a lecture verbatim is not the
  deliverable here.

## Reference files in this folder

- `chem/maps.json` — chapter ↔ NCERT file ↔ video ID map, plus the one artifact title and
  favicon per chapter. Copy values from here; do not re-derive them.
- `chem/published.json` — per-chapter build state (`url`, `has_lecture`, `has_pyq`). Read and
  update this on every video. It is tracked in git, not gitignored — it is the only record of
  progress across sessions.
- `chem/template.html` — the artifact skeleton. Slots are `{{LIKE_THIS}}`. Fill it in, don't
  restructure the CSS/script parts.
- `chem/qa.py` — run this before every publish: `python3 chem/qa.py chem/build/ch<N>.html
  --stage lecture|pyq|final`. Fix every FAIL before publishing.
- `chem/transcripts/` — save each pasted transcript here as `ch<N>-<pyq|oneshot>.txt`
  (gitignored).
- `chem/build/` — local copy of the generated HTML, `ch<N>.html` (gitignored).

## 1. Prior-knowledge rule — the most important rule in this file

The user was once handed a technically correct Coordination Compounds summary written in
revision style, and it read as gibberish — revision notes assume prior learning the user didn't
have. Guard against exactly that.

Before writing any line, ask: **could a student who has never heard this word follow this
sentence?**

- **Chapters 4, 5, 6** (d and f Block, Coordination Compounds, Haloalkanes) — assume the answer
  is NO for every technical term. Tag it **`[exposure]`** (use the `exposure-tag` span in the
  template) and give it **four to six lines**: (1) what it is in plain words, (2) why it exists
  / what problem it solves, (3) one concrete example with real formulae or numbers.
- **Chapters 1, 2, 3** (Solutions, Electrochemistry, Kinetics) — the student has already met the
  theory. **Never** use `[exposure]` here. Still teach the concept properly, but keep the
  concept statement tight and spend the length on **numerical method** — that's the actual gap.

## 2. PYQ section — required structure, exactly four parts, appended LAST

This is not a separate artifact. It is the final part of the chapter's one combined artifact,
after the lecture content and its numerical-patterns-collected closer. Still format it visibly
differently from the teaching sections above it — a past-questions video is not a chapter and
shouldn't read like one, even sharing a page with one.

In this exact order:

1. **Question types**, ranked by how often they appear. Per type: one-line recognition cue →
   numbered method steps → **the trap**.
2. **Mark slots** — which slot each type belongs to (1-marker / 2 / 3 / 4-mark case study / one
   of the three 5-markers). Take it from what the video states; if the video doesn't state
   marks, infer from question shape and mark it `(inferred)`.
3. **Repeat offenders** — questions or near-identical variants that appeared more than once
   across years. Highest-probability items in the chapter; give them a visually distinct
   section (the `.repeat-item` styling, using `--repeat`).
4. **Numerical types** — **one fully worked example per type**, then **three or four more
   questions with answers only, no working**. One model per pattern, then the student goes cold.
   Do not work every question.

Refer to questions as **year + number** (`2023 Q17`, `2019 Q5(b)`). Never reprint long question
text — one line of paraphrase, maximum.

## 3. Lecture section — required structure, comes FIRST

Follow the chapter's own teaching order, the order Sourabh sir gives it in — do not reorder to
match the NCERT chapter structure. Per topic:

concept (depth per §1) → the formula or reaction (KaTeX/mhchem) → one worked example if the
topic is numerical → what the examiner asks from this topic.

Close with **one** "Numerical patterns, collected" section gathering every worked pattern from
the chapter in one place. This section is heaviest for Chapters 1–3.

## 3a. Building one chapter artifact across two transcripts

The lecture and PYQ transcripts for a chapter can arrive in either order, in separate turns,
with other chapters' transcripts in between. `chem/published.json` is the source of truth for
where each chapter stands. On every video:

1. Look up the chapter's entry in `chem/published.json`.
2. **First transcript for this chapter** (`url` is `null`): build only the section that
   transcript covers (lecture per §3, or PYQ per §2) into `chem/template.html`. Leave the other
   section's placeholder block out entirely — delete it, don't stub it. Publish as a new
   Artifact using the `artifact_title` and `favicon` from `chem/maps.json` for this chapter.
   Write the returned URL into `published.json`, and flip `has_lecture` or `has_pyq` to `true`.
3. **Second transcript for this chapter** (`url` already set): use the Artifact tool's `read`
   action on that `url` to fetch the currently published HTML. Insert the new section in the
   correct position — lecture content always precedes the PYQ section, regardless of which was
   written first. Publish again, passing the same `url`, so it updates in place instead of
   creating a duplicate. Flip the remaining flag to `true`.
4. A chapter is done once `url` is set and both flags are `true`. Run `chem/qa.py --stage final`
   against the published content (read it back, don't trust the local `chem/build/` copy, which
   may predate the merge).

## 4. Style constraints — checkable, not vibes

- Short sentences. Plain words. If a line takes two reads to parse, rewrite it.
- No jargon unless NCERT or Xam Idea uses that exact term. If unavoidable: define inline in five
  words, once, then move on.
- No introductions. No "in this video we will". No summary of the summary.
- Never reprint the syllabus back at the reader.

## 5. Chemistry rendering rules

- **Chemical equations and formulae → mhchem**: `$\ce{2H2 + O2 -> 2H2O}$`,
  `$\ce{[Co(NH3)6]^3+}$`. Handles subscripts, charges, arrows, states correctly.
- **Maths → plain KaTeX**: Nernst, Arrhenius, `$\Delta T_f = K_f \cdot m$`, rate laws.
- The three KaTeX/mhchem/auto-render scripts and their order are already correct in
  `chem/template.html` — do not touch them.
- Delimiters already wired in the template: `$$…$$` display, `$…$` inline, `throwOnError:
  false`. `renderMathInElement` is already scoped to `#chem-content`, not `document.body`.

## 6. NCERT cross-check — when and how

Check against NCERT when: a term's spelling or definition matters, a formula or constant is
being stated, an IUPAC name is given, or the transcript sounds garbled.

1. Call `mcp__Google_Drive__read_file_content` with the chapter's `ncert_fileId` from
   `chem/maps.json`.
2. It will exceed the token cap and report a saved local file path. Use that path.
3. `grep` the saved file for distinctive words — not exact section-number strings, because of
   drop-cap artifacts.
4. **NCERT is authoritative for**: term spelling, definitions, IUPAC names, standard formulae,
   constants, section numbering.
5. **NCERT is NOT the source for**: teaching order, exam technique, question selection. Sourabh
   sir's material governs those — NCERT is for checks, not the material itself.
6. Equations inside the extracted NCERT text are unreliable — write the canonical correct
   formula yourself; don't trust one copied from the extraction.

## 7. Transcript defect handling — no board frames to fall back on

- **Garbled technical term** (auto-captions mangle Hinglish chemistry badly — e.g. "lanthanoid
  contraction" → "lantern node contraction"): correct it via NCERT. Never propagate a garbled
  term into the notes.
- **Repeated block**: caption loops happen. Repetition is not emphasis — write the content once.
- **Transcript ends mid-topic**: say so in the artifact at the cut-off point, and tell the user.
- **Suspiciously short transcript** for a one-shot chapter: flag it and ask before writing.
- **Transcript content doesn't match the claimed chapter**: stop and confirm with the user
  rather than producing a whole wrong artifact.
- **A number you cannot verify**: write it with a short "verify" marker rather than guessing.

## 8. Design system — already built into chem/template.html

Phone-first: single column, ~62ch measure, `<summary>` tap targets ≥44px tall. Every top-level
section is a `<details>`, **closed by default**. `<summary>` = section name + a short "what's
inside" line.

Theming is the three-block cascade already in the template — bare `:root` (light) →
`@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {…} }` →
`:root[data-theme="dark"] {…}`. Don't add a token anywhere except duplicated across all three
blocks; a token defined only inside a media query is the classic unreadable-artifact bug.
`body` sets `background` from a token — already wired.

Tokens already defined (don't invent new ones without adding them to all three blocks):
`--bg --surface --surface-alt --text --text-muted --border --accent --accent-soft --trap
--trap-soft --repeat --repeat-soft`.

`--trap` styles trap callouts (`.trap`). `--repeat` is reserved for the Repeat Offenders section
only (`.repeat-item`), so the highest-value items are visually unmistakable.

Type: IBM Plex Sans (headings/UI) · Public Sans (body) · IBM Plex Mono (year-question refs,
mark-slot badges, data) — already wired via the Google Fonts `<link>` in the template head.

Load the `artifact-design` skill before writing the first artifact this session.

## 9. Per-video execution checklist

1. Identify the video from `chem/maps.json` (chapter + type: lecture/one-shot or PYQ). Confirm
   the transcript's actual content matches that chapter before writing anything.
2. Save the transcript to `chem/transcripts/ch<N>-<pyq|oneshot>.txt`. Strip timestamps.
3. Skim for defects from §7 first, not after writing.
4. Pull the chapter's NCERT file per §6 and keep the saved path handy for spot-checks.
5. Draft content per §2 (PYQ section) or §3 (lecture section), applying §1 depth rules
   throughout. Write original teaching prose grounded in the transcript.
6. Check `chem/published.json` for this chapter and follow §3a.
7. Fill `chem/template.html`, write the result to `chem/build/ch<N>.html`.
8. Run `python3 chem/qa.py chem/build/ch<N>.html --stage <lecture|pyq|final>`. Fix every FAIL.
9. Publish per §3a, update `chem/published.json`, and give the user the link. If this was the
   second transcript for the chapter, say explicitly that the chapter is complete.

## 10. Pre-publish QA — scripted in chem/qa.py, run it, don't eyeball it

`chem/qa.py` checks: no doctype/html/head/body wrapper; no top-level `<details open>`; every
`var(--token)` used is defined in the bare `:root` block; both dark blocks present; `body` sets
`background` from a token; `<title>` matches `chem/maps.json`'s `artifact_title` exactly; the
three KaTeX scripts present and in order; `renderMathInElement`'s target id exists; `[exposure]`
present for Ch 4/5/6 and absent for Ch 1/2/3; no sentence starts "In this video"; file under
16 MB. Additionally verify by eye, since the script can't check these:

- PYQ section (once present): all four parts, in order, appended after the lecture content —
  never interleaved with it.
- Each numerical type in the PYQ section has **exactly one** worked example; extras are
  answer-only.
- Questions referenced as year + number; no long question text reprinted.
- No verbatim transcript sentence appears in the artifact — spot-compare a few lines against
  `chem/transcripts/`.
- `chem/published.json` for this chapter matches reality (`url` set, flags correct).

## Verification

- **Pilot with a first-contact chapter (4, 5, or 6), not Ch 1 — and pilot the full chapter,
  both transcripts**, so the §3a read-then-update-in-place flow is exercised at least once
  before repeating it five more times unattended. Publish, have the user read it on a phone, and
  confirm the `[exposure]` depth is right before building the other five chapters.
- Confirm on the published page (not the local file — `file://` cannot reach cdnjs) that KaTeX
  and mhchem actually render: one `\ce{}` equation and one display formula.
- Toggle light/dark and confirm both are legible, including formula glyph colour.
- Spot-check one NCERT-verified term per artifact against the grep result.
- After the pilot chapter is signed off, the template is frozen — the remaining five chapters
  reuse it unchanged.
