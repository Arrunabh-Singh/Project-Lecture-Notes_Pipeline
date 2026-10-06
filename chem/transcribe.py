"""Gemini ASR for one chemistry lecture, given a LOCAL audio/video file.

This does not touch YouTube or Google Drive itself -- both are out of this
script's scope on purpose:
  - YouTube fetch is IP-blocked in the cloud environment this was first built
    in (confirmed three ways: yt-dlp captions, yt-dlp audio-only extraction,
    youtube-transcript-api's explicit "IpBlocked" error). Nothing here works
    around that.
  - A Drive file has to be pulled to local disk first -- do that step first,
    then pass the resulting local path to this script.

Reuses the physics pipeline's ASR client as-is (lecturepipe/asr/gemini.py,
lecturepipe/asr/verify.py, lecturepipe/media.py) rather than rebuilding it --
same Files API upload, same 429/503 retry, same fabricated-tail sanitize
logic (see verify.py's docstring: a cheap model invented plausible extra
content past the true audio duration on a real physics lecture; that risk
is generic to any Gemini ASR call, not physics-specific).

Usage:
    python3 chem/transcribe.py <audio_or_video_path> --chapter 4 --type oneshot
    python3 chem/transcribe.py <path> --chapter 6 --type pyq --no-cache
    python3 chem/transcribe.py <path> --chapter 8 --type pyq2025
    python3 chem/transcribe.py <path> --chapter 7 --type oneshot --force-chunk

Verify and repair a finished transcript (needs no model call except --clip):
    python3 chem/transcribe.py --chapter 7 --type oneshot --report
    python3 chem/transcribe.py <path> --chapter 7 --type oneshot --clip 1800 1860
    python3 chem/transcribe.py --chapter 7 --type oneshot --splice 1800 1860

Writes the flat transcript to chem/transcripts/ch<N>-<type>.txt and the
timestamped one to ch<N>-<type>.segments.json. Does NOT write notes or touch
the artifact -- that's still a separate, human-in-the-loop step per
chem/SKILL.md, because the whole point of that spec (depth calibration,
teaching order, NCERT cross-check) is judgement this script has no way to
apply.

Exit code 75 means the model's daily quota ran out. Finished chunks are
checkpointed (chem/transcripts/chunks/), so re-running with
GEMINI_MODEL=gemini-3.5-flash-lite resumes from the first unfinished chunk.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lecturepipe.asr.gemini import (
    GeminiASRError, GeminiAuthError, Transcript, TranscriptSegment, transcribe_lecture,
)
from lecturepipe.asr.verify import (
    COVERAGE_THRESHOLD, DURATION_GRACE_SECONDS, chunk_boundaries, check_coverage,
)
from lecturepipe.config import config
from lecturepipe.media import MediaError, extract_audio, probe_duration_seconds, slice_audio

CHEM_DIR = Path(__file__).resolve().parent
TRANSCRIPTS_DIR = CHEM_DIR / "transcripts"
CHUNKS_DIR = TRANSCRIPTS_DIR / "chunks"
CLIPS_DIR = TRANSCRIPTS_DIR / "clips"
AUDIO_CACHE_DIR = CHEM_DIR / "build" / "audio_cache"

# Above this fraction of verbatim-repeated lines, treat the transcript as
# looped rather than merely repetitive. Chosen from this batch's observed
# split: clean files sat at 0-4% (a teacher genuinely repeating a point),
# while the three looped ones were 10.9%, 17.9% and 27.6%.
DUPLICATION_THRESHOLD = 0.06

# A silence between two segments longer than this is either clock drift or
# speech the model skipped -- it has to be re-transcribed on its own to tell.
GAP_SECONDS = 30.0

# Plausible Hinglish teaching pace, in words per TRUE second of audio. Used to
# decide whether a chunk whose timestamps overshoot its length is real speech
# on a fast clock (rescale it) or an invented tail (let sanitize cut it).
MIN_WPS, MAX_WPS = 1.2, 4.5

EXIT_QUOTA = 75


def _chapter_name(chapter_num: str) -> str:
    maps = json.loads((CHEM_DIR / "maps.json").read_text(encoding="utf-8"))
    entry = next((c for c in maps["chapters"] if str(c["number"]) == chapter_num), None)
    if entry is None:
        raise SystemExit(f"chapter {chapter_num} not found in chem/maps.json")
    return entry["name"]


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", text.lower()).strip()


def duplication_ratio(segments: list[TranscriptSegment]) -> float:
    """Fraction of substantial lines that are verbatim repeats of an earlier
    line. Catches the failure mode neither the coverage check nor
    verify.py's sanitize can see: Gemini looping back to re-emit an earlier
    stretch of the lecture while its timestamps keep advancing. No gap, no
    ADJACENT duplicate (the repeated lines aren't next to each other), so
    both existing checks pass -- while whole minutes of real content are
    replaced by a repeat and silently lost.

    Found live on this batch: ch4-pyq had questions 4-8 emitted three times
    each and questions 9-12 missing entirely, at a reported 100.3% coverage.
    """
    lines = [_norm(s.text) for s in segments]
    lines = [l for l in lines if len(l) > 40]  # short lines repeat innocently
    if not lines:
        return 0.0
    counts = Counter(lines)
    duplicated = sum(c - 1 for c in counts.values() if c > 1)
    return duplicated / len(lines)


def repeat_runs(segments: list[TranscriptSegment], min_run: int = 3) -> list[tuple[float, float]]:
    """Time ranges where `min_run`+ consecutive lines are repeats of earlier
    lines -- i.e. where to look for a loop when duplication is high."""
    seen: set[str] = set()
    flags = []
    for s in segments:
        n = _norm(s.text)
        dup = len(n) > 40 and n in seen
        seen.add(n)
        flags.append(dup)
    runs, i = [], 0
    while i < len(flags):
        if flags[i]:
            j = i
            while j + 1 < len(flags) and flags[j + 1]:
                j += 1
            if j - i + 1 >= min_run:
                runs.append((segments[i].start_seconds, segments[j].end_seconds))
            i = j + 1
        else:
            i += 1
    return runs


def find_gaps(segments: list[TranscriptSegment], duration: float) -> list[tuple[float, float]]:
    """Every stretch longer than GAP_SECONDS with no transcript, including the
    head and tail of the audio."""
    gaps, prev_end = [], 0.0
    for s in sorted(segments, key=lambda s: s.start_seconds):
        if s.start_seconds - prev_end > GAP_SECONDS:
            gaps.append((prev_end, s.start_seconds))
        prev_end = max(prev_end, s.end_seconds)
    if duration - prev_end > GAP_SECONDS:
        gaps.append((prev_end, duration))
    return gaps


def _wps(segments: list[TranscriptSegment], duration: float) -> float:
    return sum(len(s.text.split()) for s in segments) / duration if duration > 0 else 0.0


def _fit_to_chunk(segments: list[TranscriptSegment], duration: float) -> tuple[list[TranscriptSegment], float]:
    """flash-lite's clock runs up to 2x fast inside a chunk, so the second half
    of real speech gets stamped past the chunk's end -- and sanitize_segments
    would then throw it away as a fabricated tail. If squeezing the whole chunk
    into its true length gives a plausible speaking rate, it was drift: rescale.
    Otherwise return it untouched and let sanitize cut the overshoot."""
    last = segments[-1].end_seconds if segments else 0.0
    if last <= duration + DURATION_GRACE_SECONDS:
        return segments, 1.0
    scale = duration / last
    if not MIN_WPS <= _wps(segments, duration) <= MAX_WPS:
        return segments, 1.0
    return [replace(s, start_seconds=s.start_seconds * scale, end_seconds=s.end_seconds * scale)
            for s in segments], scale


def _attempt(chunk_path: Path, chapter_name: str, lexicon: list[str], duration: float, use_cache: bool) -> dict:
    t = transcribe_lecture(chunk_path, chapter_name, lexicon, use_cache=use_cache, subject="Chemistry")
    fitted, scale = _fit_to_chunk(t.segments, duration)
    cov = check_coverage(Transcript(fitted, t.source_audio_sha256, t.cache_hit), duration)
    kept = cov.sanitize.segments if cov.sanitize else fitted
    dup = duplication_ratio(kept)
    return dict(segments=kept, scale=scale, coverage=cov.coverage_ratio, dup=dup,
                wps=_wps(kept, duration), ok=cov.passed and dup <= DUPLICATION_THRESHOLD)


def _transcribe_chunked(
    wav_path: Path, tag: str, chapter_name: str, lexicon: list[str], duration: float,
    use_cache: bool, chunk_seconds: float,
) -> tuple[list[TranscriptSegment], list[dict]]:
    """Fallback for when a single-shot Gemini call under-covers the audio
    (see lecturepipe/asr/verify.py's docstring: silent truncation is a real,
    seen-live failure mode, not hypothetical). Splits into fixed chunks,
    transcribes each independently, and re-offsets each chunk's segment
    timestamps back into the full lecture's timeline.

    Every finished chunk is checkpointed with the model that produced it, so a
    run that dies on the daily quota resumes where it stopped -- and so the
    final report can say exactly which model each stretch came from."""
    boundaries = chunk_boundaries(duration, chunk_seconds=chunk_seconds)
    chunk_dir = wav_path.parent / f"{wav_path.stem}_chunks"
    chunk_dir.mkdir(parents=True, exist_ok=True)
    ckpt_dir = CHUNKS_DIR / tag
    ckpt_dir.mkdir(parents=True, exist_ok=True)
    all_segments: list[TranscriptSegment] = []
    meta: list[dict] = []
    max_chunk_attempts = 3

    for i, (start, end) in enumerate(boundaries):
        ckpt = ckpt_dir / f"chunk_{i:03d}_{int(chunk_seconds)}.json"
        if use_cache and ckpt.exists():
            saved = json.loads(ckpt.read_text(encoding="utf-8"))
            print(f"    chunk {i + 1}/{len(boundaries)} [{start:.0f}s-{end:.0f}s] resumed "
                  f"({saved['model']}, coverage {saved['coverage']:.1%})", flush=True)
            chunk_segments = [TranscriptSegment(**s) for s in saved["segments"]]
            info = {k: v for k, v in saved.items() if k != "segments"}
        else:
            chunk_path = chunk_dir / f"chunk_{i:03d}.wav"
            slice_audio(wav_path, chunk_path, start, end)
            best = None
            for attempt in range(max_chunk_attempts):
                # Attempt 0 may hit cache (free if this exact chunk was already
                # transcribed by this model). A bad cached result would repeat
                # forever, so every retry forces a fresh call.
                print(f"    chunk {i + 1}/{len(boundaries)} [{start:.0f}s-{end:.0f}s] "
                      f"(attempt {attempt + 1}/{max_chunk_attempts}, {config.gemini_model}) ...", flush=True)
                r = _attempt(chunk_path, chapter_name, lexicon, end - start, use_cache and attempt == 0)
                print(f"      coverage {r['coverage']:.1%}, duplication {r['dup']:.1%}, "
                      f"{r['wps']:.2f} words/s, clock x{r['scale']:.2f}, {len(r['segments'])} segments", flush=True)
                if best is None or (r["ok"], r["coverage"] - r["dup"]) > (best["ok"], best["coverage"] - best["dup"]):
                    best = r
                if r["ok"]:
                    break
                print("      under threshold or looped -- retrying this chunk fresh ...", flush=True)
            if not best["ok"]:
                print(f"    *** chunk {i + 1} still bad after {max_chunk_attempts} attempts -- keeping best "
                      f"available; it will show up in --report. Flag per chem/SKILL.md section 7. ***", flush=True)
            chunk_segments = best["segments"]
            info = dict(index=i, start=start, end=end, model=config.gemini_model,
                        **{k: best[k] for k in ("scale", "coverage", "dup", "wps", "ok")})
            ckpt.write_text(json.dumps({**info, "segments": [s.__dict__ for s in chunk_segments]},
                                       ensure_ascii=False), encoding="utf-8")
        meta.append(info)
        all_segments += [replace(s, start_seconds=s.start_seconds + start, end_seconds=s.end_seconds + start)
                         for s in chunk_segments]
    return all_segments, meta


# ---------------------------------------------------------------- outputs

def _paths(tag: str) -> tuple[Path, Path]:
    return TRANSCRIPTS_DIR / f"{tag}.txt", TRANSCRIPTS_DIR / f"{tag}.segments.json"


def _write_outputs(tag: str, segments: list[TranscriptSegment], duration: float, extra: dict) -> None:
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    txt, js = _paths(tag)
    txt.write_text("\n".join(s.text for s in segments), encoding="utf-8")
    js.write_text(json.dumps({"segments": [s.__dict__ for s in segments], "true_duration_seconds": duration,
                              **extra}, indent=2, ensure_ascii=False), encoding="utf-8")


def _load(tag: str) -> tuple[list[TranscriptSegment], float, dict]:
    _, js = _paths(tag)
    if not js.exists():
        raise SystemExit(f"no transcript yet: {js}")
    d = json.loads(js.read_text(encoding="utf-8"))
    extra = {k: v for k, v in d.items() if k not in ("segments", "true_duration_seconds")}
    return [TranscriptSegment(**s) for s in d["segments"]], d["true_duration_seconds"], extra


def _hms(sec: float) -> str:
    sec = int(sec)
    return f"{sec // 3600}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def report(tag: str) -> dict:
    """The numbers behind the PR's per-file verification table."""
    segments, duration, extra = _load(tag)
    reach = (segments[-1].end_seconds / duration) if segments else 0.0
    dup = duplication_ratio(segments)
    gaps = find_gaps(segments, duration)
    ordered = sorted(segments, key=lambda s: s.start_seconds)
    inner = [b.start_seconds - a.end_seconds for a, b in zip(ordered, ordered[1:])]
    max_gap = max([0.0, *inner, *(e - s for s, e in gaps)])
    chunks = extra.get("chunks", [])
    models = Counter(c["model"] for c in chunks) or Counter({extra.get("model", "?"): 1})
    bad_chunks = [c["index"] + 1 for c in chunks if not c["ok"]]
    drifted = [c["index"] + 1 for c in chunks if c["scale"] != 1.0]
    odd_rate = [c["index"] + 1 for c in chunks if not MIN_WPS <= c["wps"] <= MAX_WPS]
    runs = repeat_runs(segments)
    low_conf = sum(1 for s in segments if s.confidence == "low")

    print(f"{tag}: {_hms(duration)} audio, {len(segments)} segments, "
          f"models {dict(models)}, chunk size {extra.get('chunk_seconds', 'single-shot')}")
    print(f"  coverage (last segment end / duration): {reach:.1%}   "
          f"{'OK' if reach >= 0.99 else 'BELOW 99%'}")
    print(f"  duplication: {dup:.1%}   {'OK' if dup < DUPLICATION_THRESHOLD else 'OVER 6%'}")
    print(f"  max gap: {max_gap:.0f}s   gaps over {GAP_SECONDS:.0f}s: "
          + (", ".join(f"{_hms(s)}-{_hms(e)} ({e - s:.0f}s)" for s, e in gaps) or "none"))
    if runs:
        print("  repeat runs (look for a loop): " + ", ".join(f"{_hms(s)}-{_hms(e)}" for s, e in runs))
    if bad_chunks:
        print(f"  chunks that never passed their own check: {bad_chunks}")
    if drifted:
        print(f"  chunks rescaled for a fast clock: {drifted}")
    if odd_rate:
        print(f"  chunks with an implausible speaking rate: {odd_rate}")
    if extra.get("splices"):
        print("  splices: " + ", ".join(f"{_hms(a)}-{_hms(b)}" for a, b in extra["splices"]))
    print(f"  low-confidence segments: {low_conf}")

    out = dict(tag=tag, duration=duration, segments=len(segments), coverage=reach, duplication=dup,
               max_gap=max_gap, gaps_over_30s=[list(g) for g in gaps], models=dict(models),
               bad_chunks=bad_chunks, drifted_chunks=drifted, odd_rate_chunks=odd_rate,
               repeat_runs=[list(r) for r in runs], low_confidence=low_conf,
               splices=extra.get("splices", []))
    (TRANSCRIPTS_DIR / f"{tag}.report.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    return out


def clip(tag: str, wav_path: Path, chapter_name: str, lexicon: list[str], start: float, end: float,
         use_cache: bool) -> None:
    """Transcribe just [start, end) on its own, in lecture time. This is how a
    gap is classified (speech already in the transcript = clock drift; speech
    not there = a skipped stretch) and how a looped stretch is repaired."""
    CLIPS_DIR.mkdir(parents=True, exist_ok=True)
    clip_wav = AUDIO_CACHE_DIR / f"{tag}_clip_{int(start)}_{int(end)}.wav"
    slice_audio(wav_path, clip_wav, start, end)
    r = _attempt(clip_wav, chapter_name, lexicon, end - start, use_cache)
    segs = [replace(s, start_seconds=s.start_seconds + start, end_seconds=s.end_seconds + start)
            for s in r["segments"]]
    base = CLIPS_DIR / f"{tag}-{int(start)}-{int(end)}"
    base.with_suffix(".json").write_text(
        json.dumps({"start": start, "end": end, "model": config.gemini_model,
                    "segments": [s.__dict__ for s in segs]}, indent=2, ensure_ascii=False), encoding="utf-8")
    base.with_suffix(".txt").write_text("\n".join(f"[{_hms(s.start_seconds)}] {s.text}" for s in segs),
                                        encoding="utf-8")
    print(f"clip {_hms(start)}-{_hms(end)} ({config.gemini_model}): coverage {r['coverage']:.1%}, "
          f"duplication {r['dup']:.1%}, {r['wps']:.2f} words/s, {len(segs)} segments -> {base}.txt")


def splice(tag: str, start: float, end: float) -> None:
    """Replace the main transcript's segments in [start, end) with the clip made
    by --clip over exactly that range."""
    cj = CLIPS_DIR / f"{tag}-{int(start)}-{int(end)}.json"
    if not cj.exists():
        raise SystemExit(f"run --clip {start:g} {end:g} first: {cj} not found")
    new = [TranscriptSegment(**s) for s in json.loads(cj.read_text(encoding="utf-8"))["segments"]]
    segments, duration, extra = _load(tag)
    keep = [s for s in segments if not start <= (s.start_seconds + s.end_seconds) / 2 < end]
    merged = sorted(keep + new, key=lambda s: s.start_seconds)
    extra["splices"] = [*extra.get("splices", []), [start, end]]
    _write_outputs(tag, merged, duration, extra)
    print(f"spliced {len(new)} clip segments over {len(segments) - len(keep)} old ones in "
          f"{_hms(start)}-{_hms(end)}")


# ------------------------------------------------------------------- main

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=Path, nargs="?", help="local audio or video file "
                        "(not needed for --report / --splice)")
    parser.add_argument("--chapter", required=True, help="chapter number, 1-10")
    parser.add_argument("--type", required=True, choices=["pyq", "pyq2025", "oneshot"])
    parser.add_argument("--no-cache", action="store_true", help="force a fresh Gemini call")
    parser.add_argument(
        "--force-chunk",
        action="store_true",
        help="skip the single-shot attempt entirely and go straight to chunked "
             "transcription -- use for anything over ~30 min, where a single shot "
             "would only burn a request on a truncated answer",
    )
    parser.add_argument("--chunk-seconds", type=float, default=600.0,
                        help="chunk length for the chunked path (default 600; use 300 on flash-lite)")
    parser.add_argument("--report", action="store_true", help="verify an existing transcript and exit")
    parser.add_argument("--clip", nargs=2, type=float, metavar=("START", "END"),
                        help="transcribe only this span (seconds) into chem/transcripts/clips/")
    parser.add_argument("--splice", nargs=2, type=float, metavar=("START", "END"),
                        help="splice the clip made for exactly this span into the transcript")
    parser.add_argument(
        "--lexicon-file",
        type=Path,
        default=None,
        help="optional newline-separated file of technical terms to prime the ASR prompt with "
             "(e.g. IUPAC names grep'd from the chapter's NCERT text). Omit for a plain, "
             "unprimed transcription -- NCERT cross-checking happens later anyway (SKILL.md 6).",
    )
    args = parser.parse_args()
    tag = f"ch{args.chapter}-{args.type}"

    if args.report:
        report(tag)
        return
    if args.splice:
        splice(tag, *args.splice)
        return

    if args.input_path is None or not args.input_path.exists():
        raise SystemExit(f"no such file: {args.input_path}")

    chapter_name = _chapter_name(args.chapter)
    lexicon = []
    if args.lexicon_file and args.lexicon_file.exists():
        lexicon = [line.strip() for line in args.lexicon_file.read_text().splitlines() if line.strip()]

    AUDIO_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    wav_path = AUDIO_CACHE_DIR / f"{tag}.wav"

    if wav_path.exists():
        duration = probe_duration_seconds(wav_path)
    else:
        print(f"Extracting/normalizing audio -> {wav_path} ...")
        try:
            extract_audio(args.input_path, wav_path)
            duration = probe_duration_seconds(wav_path)
        except MediaError as exc:
            raise SystemExit(f"ffmpeg step failed: {exc}") from exc
    print(f"  duration: {duration:.1f}s ({duration / 60:.1f} min)")

    try:
        if args.clip:
            clip(tag, wav_path, chapter_name, lexicon, *args.clip, use_cache=not args.no_cache)
            return
        run_transcription(args, tag, wav_path, chapter_name, lexicon, duration)
    except GeminiAuthError as exc:
        raise SystemExit(f"Gemini auth error -- check GEMINI_API_KEY in .env: {exc}") from exc
    except GeminiASRError as exc:
        print(f"Gemini ASR failed on {config.gemini_model}: {exc}", flush=True)
        # Finished chunks are checkpointed; re-run (same command) to resume.
        sys.exit(EXIT_QUOTA if "quota" in str(exc).lower() else 1)


def run_transcription(args, tag: str, wav_path: Path, chapter_name: str, lexicon: list[str],
                      duration: float) -> None:
    sanitize = None
    chunk_meta: list[dict] = []
    needs_chunking = args.force_chunk
    transcript = None

    if not args.force_chunk:
        print(f"Calling Gemini (subject=Chemistry, chapter={chapter_name!r}, model={config.gemini_model}, "
              f"lexicon terms={len(lexicon)}, cache={'off' if args.no_cache else 'on'}) ...")
        transcript = transcribe_lecture(
            wav_path, chapter_name, lexicon, use_cache=not args.no_cache, subject="Chemistry",
        )
        print(f"  cache hit: {transcript.cache_hit}, raw segments: {len(transcript.segments)}")
        fitted, scale = _fit_to_chunk(transcript.segments, duration)
        if scale != 1.0:
            print(f"  clock ran fast: rescaled x{scale:.2f}")
        transcript = Transcript(fitted, transcript.source_audio_sha256, transcript.cache_hit)

        coverage = check_coverage(transcript, duration)
        sanitize = coverage.sanitize
        print(f"  coverage: {coverage.coverage_ratio:.1%} "
              f"({coverage.covered_seconds:.0f}s / {coverage.true_duration_seconds:.0f}s)")
        if sanitize and (sanitize.dropped_past_duration or sanitize.dropped_repetition):
            print(f"  sanitize: dropped {sanitize.dropped_past_duration} past-duration, "
                  f"{sanitize.dropped_repetition} repetition segments")
        print(f"  low-confidence segments: {coverage.low_confidence_count}")

        single_shot_dupes = duplication_ratio(sanitize.segments if sanitize else transcript.segments)
        print(f"  duplicated content: {single_shot_dupes:.1%}")
        needs_chunking = not coverage.passed or single_shot_dupes > DUPLICATION_THRESHOLD
        if needs_chunking:
            if not coverage.passed:
                reason = f"coverage below threshold ({coverage.coverage_ratio:.1%})"
            else:
                # Coverage alone would have called this file fine. It isn't:
                # the model looped and re-emitted earlier content in place of
                # real lecture material, which coverage cannot see.
                reason = f"looped output ({single_shot_dupes:.1%} duplicated) despite passing coverage"
            print(f"\n  {reason} -- falling back to chunked transcription ...")

    if needs_chunking:
        n_chunks = len(chunk_boundaries(duration, args.chunk_seconds))
        print(f"  chunked transcription: {n_chunks} chunks of {args.chunk_seconds:.0f}s, "
              f"model {config.gemini_model}")
        # Each chunk was already sanitized independently inside
        # _transcribe_chunked (that's the correct scope for the
        # "everything after a detected repeat/fabrication is untrustworthy"
        # rule -- it applies within one continuous Gemini response). Do NOT
        # re-run check_coverage's sanitize_segments on the concatenated
        # result: that rule is wrong across independently-transcribed
        # chunks, where an adjacent near-duplicate at a chunk boundary
        # (plausible given ffmpeg's seek isn't sample-exact) would wrongly
        # truncate every later chunk's real content, not just the
        # boundary artifact.
        segments, chunk_meta = _transcribe_chunked(
            wav_path, tag, chapter_name, lexicon, duration, use_cache=not args.no_cache,
            chunk_seconds=args.chunk_seconds,
        )
    else:
        segments = sanitize.segments if sanitize else transcript.segments

    extra = {"model": config.gemini_model}
    if chunk_meta:
        extra.update(chunks=chunk_meta, chunk_seconds=args.chunk_seconds)
    _write_outputs(tag, segments, duration, extra)
    txt, js = _paths(tag)
    print(f"\nWrote flat transcript -> {txt}\nWrote timestamped segments -> {js}\n")
    result = report(tag)
    if result["coverage"] < COVERAGE_THRESHOLD or result["duplication"] > DUPLICATION_THRESHOLD:
        print("\n*** This transcript fails its checks -- repair it (--clip / --splice) or flag it per "
              "chem/SKILL.md section 7 before drafting notes from it. ***")
    print("\nThis is raw ASR output -- treat it exactly like a pasted transcript from here: "
          "apply chem/SKILL.md section 7 (defect handling) before drafting notes, and note "
          "any low-confidence or garbled spans against NCERT before trusting them.")


if __name__ == "__main__":
    main()
