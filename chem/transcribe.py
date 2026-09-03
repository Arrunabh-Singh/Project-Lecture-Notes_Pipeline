"""Gemini ASR for one chemistry lecture, given a LOCAL audio/video file.

This does not touch YouTube or Google Drive itself -- both are out of this
script's scope on purpose:
  - YouTube fetch is IP-blocked in this environment (confirmed three ways:
    yt-dlp captions, yt-dlp audio-only extraction, youtube-transcript-api's
    explicit "IpBlocked" error). Nothing here works around that.
  - A Drive file has to be pulled to local disk first via the
    mcp__Google_Drive__* tools (the orchestrating Claude session has those;
    a plain Python script does not) -- do that step first, then pass the
    resulting local path to this script.

Reuses the physics pipeline's ASR client as-is (lecturepipe/asr/gemini.py,
lecturepipe/asr/verify.py, lecturepipe/media.py) rather than rebuilding it --
same Files API upload, same 429/503 retry, same fabricated-tail sanitize
logic (see verify.py's docstring: a cheap model invented plausible extra
content past the true audio duration on a real physics lecture; that risk
is generic to any Gemini ASR call, not physics-specific).

Usage:
    python3 chem/transcribe.py <audio_or_video_path> --chapter 4 --type oneshot
    python3 chem/transcribe.py <path> --chapter 6 --type pyq --no-cache

Writes the flat transcript to chem/transcripts/ch<N>-<pyq|oneshot>.txt and
prints a coverage report. Does NOT write notes or touch the artifact --
that's still a separate, human-in-the-loop step per chem/SKILL.md, because
the whole point of that spec (depth calibration, teaching order, NCERT
cross-check) is judgement this script has no way to apply.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lecturepipe.asr.gemini import GeminiASRError, GeminiAuthError, transcribe_lecture
from lecturepipe.asr.verify import check_coverage
from lecturepipe.media import MediaError, extract_audio, probe_duration_seconds

CHEM_DIR = Path(__file__).resolve().parent
TRANSCRIPTS_DIR = CHEM_DIR / "transcripts"
AUDIO_CACHE_DIR = CHEM_DIR / "build" / "audio_cache"


def _chapter_name(chapter_num: str) -> str:
    maps = json.loads((CHEM_DIR / "maps.json").read_text(encoding="utf-8"))
    entry = next((c for c in maps["chapters"] if str(c["number"]) == chapter_num), None)
    if entry is None:
        raise SystemExit(f"chapter {chapter_num} not found in chem/maps.json")
    return entry["name"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=Path, help="local audio or video file")
    parser.add_argument("--chapter", required=True, help="chapter number, 1-6")
    parser.add_argument("--type", required=True, choices=["pyq", "oneshot"])
    parser.add_argument("--no-cache", action="store_true", help="force a fresh Gemini call")
    parser.add_argument(
        "--lexicon-file",
        type=Path,
        default=None,
        help="optional newline-separated file of technical terms to prime the ASR prompt with "
             "(e.g. IUPAC names grep'd from the chapter's NCERT text). Omit for a plain, "
             "unprimed transcription -- NCERT cross-checking happens later anyway (SKILL.md 6).",
    )
    args = parser.parse_args()

    if not args.input_path.exists():
        raise SystemExit(f"no such file: {args.input_path}")

    chapter_name = _chapter_name(args.chapter)
    lexicon = []
    if args.lexicon_file and args.lexicon_file.exists():
        lexicon = [line.strip() for line in args.lexicon_file.read_text().splitlines() if line.strip()]

    AUDIO_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    wav_path = AUDIO_CACHE_DIR / f"ch{args.chapter}-{args.type}.wav"

    print(f"Extracting/normalizing audio -> {wav_path} ...")
    try:
        extract_audio(args.input_path, wav_path)
        duration = probe_duration_seconds(wav_path)
    except MediaError as exc:
        raise SystemExit(f"ffmpeg step failed: {exc}") from exc
    print(f"  duration: {duration:.1f}s ({duration / 60:.1f} min)")

    print(f"Calling Gemini (subject=Chemistry, chapter={chapter_name!r}, "
          f"lexicon terms={len(lexicon)}, cache={'off' if args.no_cache else 'on'}) ...")
    try:
        transcript = transcribe_lecture(
            wav_path, chapter_name, lexicon, use_cache=not args.no_cache, subject="Chemistry",
        )
    except GeminiAuthError as exc:
        raise SystemExit(f"Gemini auth error -- check GEMINI_API_KEY in .env: {exc}") from exc
    except GeminiASRError as exc:
        raise SystemExit(f"Gemini ASR failed: {exc}") from exc

    print(f"  cache hit: {transcript.cache_hit}, raw segments: {len(transcript.segments)}")

    coverage = check_coverage(transcript, duration)
    sanitize = coverage.sanitize
    print(f"  coverage: {coverage.coverage_ratio:.1%} "
          f"({coverage.covered_seconds:.0f}s / {coverage.true_duration_seconds:.0f}s)")
    if sanitize and (sanitize.dropped_past_duration or sanitize.dropped_repetition):
        print(f"  sanitize: dropped {sanitize.dropped_past_duration} past-duration, "
              f"{sanitize.dropped_repetition} repetition segments")
    print(f"  low-confidence segments: {coverage.low_confidence_count}")

    if not coverage.passed:
        print(
            "\n*** COVERAGE BELOW THRESHOLD -- likely truncated. This script does not "
            "implement the chunk-fallback path (physics-specific, unused here so far). "
            "Inspect the output below; if it's genuinely incomplete, flag it per "
            "chem/SKILL.md section 7 (\"transcript ends mid-topic\") rather than treating "
            "it as complete. ***\n"
        )

    segments = sanitize.segments if sanitize else transcript.segments
    flat_text = "\n".join(s.text for s in segments)
    out_path = TRANSCRIPTS_DIR / f"ch{args.chapter}-{args.type}.txt"
    out_path.write_text(flat_text, encoding="utf-8")

    segments_path = TRANSCRIPTS_DIR / f"ch{args.chapter}-{args.type}.segments.json"
    segments_path.write_text(
        json.dumps(
            {"segments": [s.__dict__ for s in segments], "true_duration_seconds": duration},
            indent=2, ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(f"\nWrote flat transcript -> {out_path} ({len(flat_text)} chars)")
    print(f"Wrote timestamped segments -> {segments_path}")
    print("\nThis is raw ASR output -- treat it exactly like a pasted transcript from here: "
          "apply chem/SKILL.md section 7 (defect handling) before drafting notes, and note "
          "any low-confidence or garbled spans against NCERT before trusting them.")


if __name__ == "__main__":
    main()
