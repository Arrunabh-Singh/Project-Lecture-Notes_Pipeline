# Project-Lecture-Notes_Pipeline

Turns a private Google Drive library of Hinglish physics lectures into
NCERT-grounded study notes: transcript + board frames + textbook cross-check,
published as per-chapter HTML artifacts with LaTeX equations and diagrams.

Full design, verified environment constraints, and the accuracy strategy are
in [`/root/.claude/plans/okay-so-you-are-snoopy-tarjan.md`](../../root/.claude/plans/okay-so-you-are-snoopy-tarjan.md)
(session-local plan file) — this README covers setup and day-to-day usage.

## Why notes synthesis isn't a CLI subcommand

Every other stage (`fetch`, `audio`, `frames`, `transcribe`) is mechanical
and scriptable. Writing the actual notes is not: it requires reading each
board frame as an image and reconciling it against the transcript and the
NCERT text, which is something an agent does, not a script. `cli.py`
produces the grounded evidence (transcript segments + deduped frames +
NCERT lexicon/sections); the notes themselves are synthesized interactively
and saved via `lecturepipe.notes.save()`.

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.example .env
```

Then fill in `.env` — see the two credentials below. Nothing else is needed:
ffmpeg comes bundled via the `imageio-ffmpeg` PyPI wheel (no `apt install`).

### 1. Drive access token (~2 min)

The lecture videos are too large for the Drive MCP connector (it returns
file bytes as inline base64 — fine for small text, unusable for a 25MB+
video). This pipeline instead talks to the Drive v3 REST API directly.

1. Open the [OAuth Playground](https://developers.google.com/oauthplayground).
2. Left panel → **Drive API v3** → tick `https://www.googleapis.com/auth/drive.readonly`.
3. **Authorize APIs** → sign in as the account the lectures were shared to.
4. **Exchange authorization code for tokens** → copy the access token (`ya29.…`)
   into `DRIVE_ACCESS_TOKEN` in `.env`.

A bare access token expires in ~1 hour. `cli.py fetch --all` downloads
everything in one run and reports throughput as it goes, so you'll know
immediately if that's not enough time — if so, fill in the
`DRIVE_REFRESH_TOKEN` / `DRIVE_CLIENT_ID` / `DRIVE_CLIENT_SECRET` trio
instead (Cloud project → OAuth client → "use your own credentials" in the
Playground) for automatic refresh.

Revoke the grant at [myaccount.google.com/permissions](https://myaccount.google.com/permissions)
when you're done with it.

### 2. Gemini API key (~1 min)

Free, no card, from [aistudio.google.com/apikey](https://aistudio.google.com/apikey).
Put it in `GEMINI_API_KEY`.

**Know before you use it:** on the free tier Google may use submitted
content to improve their products. This pipeline sends lecture audio
through this key. If that's not acceptable for this content, the
alternative is local Whisper — needs `huggingface.co` reachable and
significant CPU time, with nothing leaving the machine.

## Usage

```bash
.venv/bin/python cli.py discover          # list the manifest, no credentials needed
.venv/bin/python cli.py fetch --all       # download every video (needs DRIVE_ACCESS_TOKEN)
.venv/bin/python cli.py audio --all       # extract audio (needs ffmpeg, no credentials)
.venv/bin/python cli.py frames --all      # extract + dedupe board frames (no credentials)
.venv/bin/python cli.py transcribe --all  # ASR via Gemini (needs GEMINI_API_KEY)
.venv/bin/python cli.py status            # progress across all tracked videos
```

Every subcommand also takes a single Drive file id instead of `--all`, for
processing one lecture at a time. All stages are resumable: state lives in
`state/<file_id>.json`, and `fetch` resumes partial downloads via HTTP Range
rather than restarting.

## NCERT grounding

`data/ncert/raw/` and `data/ncert/processed/` hold the extracted text and
parsed outline (section tree, lexicon, named scientists, Summary, Exercises)
for all 8 chapters — fetched once via the Drive connector's
`read_file_content` on each chapter PDF, committed so they never need
re-fetching. Regenerate the parsed outline from raw text with:

```bash
.venv/bin/python -m lecturepipe.ncert.outline
```

**Equations are not reliable in the NCERT text extraction** — figure
captions interleave into body text and formulas can scramble. NCERT is
authoritative for terminology, section structure, and exercises; board
frames (read directly as images during notes synthesis) are the source of
truth for every equation that appears in the notes.

## Layout

```
lecturepipe/
  config.py, state.py     env/paths, per-video checkpoint state
  sources/{base,gdrive,ytdlp}.py   media sources (Drive REST API; yt-dlp
                                    for Vimeo/YouTube, currently blocked by
                                    this environment's network policy)
  ncert/outline.py         NCERT raw-text -> structured JSON parser
  media.py                 ffmpeg: audio extraction, scene-detect + coverage-floor frames
  asr/{gemini,verify}.py   Gemini transcription, coverage validation
  frames.py                perceptual-hash frame dedupe
  notes.py, crosscheck.py  grounded notes schema, NCERT coverage-gap analysis
cli.py                     mechanical pipeline stages (see Usage above)
data/ncert/                committed: NCERT raw text + parsed outlines
data/lecture_manifest.json committed: all 59 lecture files (id/title/size)
data/lectures/, data/cache/  gitignored: video/audio/frames/ASR cache
notes/                      committed: per-lecture .md + notes.json (once synthesized)
tests/                      unit tests for the credential-free logic
```

## Tests

```bash
.venv/bin/python tests/test_asr_verify.py
```

Covers cache-key logic, coverage validation, chunk-boundary math, and prompt
construction — everything that doesn't require live Drive/Gemini
credentials. The media pipeline (ffmpeg audio/frame extraction) and frame
dedupe were validated manually against synthetic test video during
development; see commit history.
