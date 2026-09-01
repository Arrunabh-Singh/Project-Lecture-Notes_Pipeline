#!/usr/bin/env python3
"""Pipeline CLI. Mechanical stages only (discover/fetch/audio/frames/
transcribe/status) -- notes synthesis and artifact publishing are agent-
driven (reading frames, writing prose) and happen interactively, not via
a subcommand. See README for that half of the workflow.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from lecturepipe import state
from lecturepipe.asr.gemini import GeminiAuthError, overwrite_cache, transcribe_lecture
from lecturepipe.asr.verify import check_coverage
from lecturepipe.config import LECTURES_DIR, MANIFEST_PATH, NCERT_DIR, config
from lecturepipe.frames import dedupe_frames
from lecturepipe.media import extract_audio, extract_scene_frames, probe_duration_seconds
from lecturepipe.sources.gdrive import DriveAuthError, DriveSource


def _load_manifest_refs():
    src = DriveSource()
    return list(src.list())


def _video_dir(ref) -> Path:
    return LECTURES_DIR / ref.chapter_id / ref.id


def cmd_discover(args) -> int:
    refs = _load_manifest_refs()
    by_chapter: dict[str, list] = {}
    for r in refs:
        by_chapter.setdefault(r.chapter_id, []).append(r)
    total_bytes = sum(r.size_bytes for r in refs)
    print(f"{len(refs)} files across {len(by_chapter)} chapters, {total_bytes / 1e9:.2f} GB total\n")
    for chapter_id, items in sorted(by_chapter.items()):
        size = sum(r.size_bytes for r in items)
        print(f"  {chapter_id}: {len(items)} files, {size / 1e6:.1f} MB")
    dupes = [r for r in refs if r.known_duplicate_of]
    if dupes:
        print(f"\nFlagged duplicates ({len(dupes)}):")
        for d in dupes:
            print(f"  {d.id} ({d.title}) -> duplicate of {d.known_duplicate_of}")
    return 0


def cmd_fetch(args) -> int:
    refs = {r.id: r for r in _load_manifest_refs()}
    targets = refs.values() if args.all else [refs[args.file_id]]
    src = DriveSource()
    for ref in targets:
        st = state.load(ref.id, ref.chapter_id, ref.title)
        dest = _video_dir(ref) / f"video{Path(ref.title).suffix}"
        if st.is_done("fetched") and dest.exists():
            print(f"SKIP (already fetched): {ref.title}")
            continue
        print(f"Fetching {ref.title} ({ref.size_bytes / 1e6:.1f} MB) ...")
        try:
            src.fetch(ref, dest)
        except DriveAuthError as e:
            print(f"AUTH ERROR: {e}", file=sys.stderr)
            return 1
        sha = DriveSource.sha256_of(dest)
        st.sha256 = sha
        st.mark_done("fetched")
        state.save(st)
        print(f"  done, sha256={sha[:12]}...")
    return 0


def cmd_audio(args) -> int:
    refs = {r.id: r for r in _load_manifest_refs()}
    targets = refs.values() if args.all else [refs[args.file_id]]
    for ref in targets:
        st = state.load(ref.id, ref.chapter_id, ref.title)
        video_path = _video_dir(ref) / f"video{Path(ref.title).suffix}"
        audio_path = _video_dir(ref) / "audio.wav"
        if not video_path.exists():
            print(f"SKIP (not fetched yet): {ref.title}")
            continue
        if st.is_done("audio_extracted") and audio_path.exists():
            print(f"SKIP (already extracted): {ref.title}")
            continue
        print(f"Extracting audio: {ref.title} ...")
        extract_audio(video_path, audio_path)
        st.duration_seconds = probe_duration_seconds(video_path)
        st.mark_done("audio_extracted")
        state.save(st)
        print(f"  done, duration={st.duration_seconds:.1f}s")
    return 0


def cmd_frames(args) -> int:
    refs = {r.id: r for r in _load_manifest_refs()}
    targets = refs.values() if args.all else [refs[args.file_id]]
    for ref in targets:
        st = state.load(ref.id, ref.chapter_id, ref.title)
        video_path = _video_dir(ref) / f"video{Path(ref.title).suffix}"
        frames_dir = _video_dir(ref) / "frames"
        if not video_path.exists():
            print(f"SKIP (not fetched yet): {ref.title}")
            continue
        if st.is_done("frames_extracted"):
            print(f"SKIP (already extracted): {ref.title}")
            continue
        print(f"Extracting frames: {ref.title} ...")
        raw_frames = extract_scene_frames(
            video_path, frames_dir, duration_seconds=st.duration_seconds,
            enable_scene_detect=args.scene_detect,
        )
        deduped = dedupe_frames(raw_frames)
        (frames_dir / "index.json").write_text(json.dumps([d.__dict__ for d in deduped], indent=2))
        st.frame_count = len(deduped)
        st.mark_done("frames_extracted")
        state.save(st)
        print(f"  done, {len(raw_frames)} raw -> {len(deduped)} deduped frames")
    return 0


def cmd_transcribe(args) -> int:
    refs = {r.id: r for r in _load_manifest_refs()}
    targets = refs.values() if args.all else [refs[args.file_id]]
    for ref in targets:
        st = state.load(ref.id, ref.chapter_id, ref.title)
        audio_path = _video_dir(ref) / "audio.wav"
        if not audio_path.exists():
            print(f"SKIP (no audio yet): {ref.title}")
            continue
        if st.is_done("transcribed") and not args.force:
            print(f"SKIP (already transcribed): {ref.title}")
            continue

        outline_path = NCERT_DIR / f"{ref.chapter_id}.json"
        lexicon, chapter_title = [], ref.chapter_id
        if outline_path.exists():
            outline = json.loads(outline_path.read_text())
            lexicon = outline["lexicon"]
            chapter_title = outline["title"]

        print(f"Transcribing: {ref.title} ...")
        try:
            transcript = transcribe_lecture(audio_path, chapter_title, lexicon)
        except GeminiAuthError as e:
            print(f"AUTH ERROR: {e}", file=sys.stderr)
            return 1
        except Exception as e:
            # One bad lecture must not abort the other 58 in a --all run.
            # Deliberately broad, not just GeminiASRError: a raw
            # requests.exceptions.ProxyError from this environment's forced
            # proxy dropping a long-held connection mid-batch took down an
            # earlier run that only caught GeminiASRError -- transcribe_lecture
            # now retries known-transient cases itself (asr/gemini.py), but
            # this is the backstop for whatever that retry logic doesn't
            # anticipate. GeminiAuthError is the one thing excluded (see
            # above): a bad key fails every remaining video identically, so
            # stopping immediately beats 58 identical failures.
            print(f"  ERROR: {type(e).__name__}: {e}", file=sys.stderr)
            st.mark_error(f"{type(e).__name__}: {e}")
            state.save(st)
            continue

        coverage = check_coverage(transcript, st.duration_seconds or 0.0)
        print(f"  {'cache hit' if transcript.cache_hit else 'transcribed'}, "
              f"coverage={coverage.coverage_ratio:.1%}, "
              f"low_confidence={coverage.low_confidence_count}")
        san = coverage.sanitize
        if san and (san.dropped_past_duration or san.dropped_repetition):
            print(
                f"  SANITIZED: dropped {san.dropped_past_duration} segment(s) past true "
                f"duration, {san.dropped_repetition} to a repetition loop"
                f"{' (loop detected)' if san.repetition_detected else ''} -- "
                f"cleaning cache so downstream reads see trustworthy content only"
            )
            overwrite_cache(transcript.source_audio_sha256, san.segments)
        if coverage.needs_chunk_fallback:
            print("  WARNING: coverage below threshold -- chunk fallback not yet wired into CLI, flagging for manual re-run")
            st.mark_error(f"low coverage: {coverage.coverage_ratio:.1%}")
        else:
            st.transcript_cache_key = transcript.source_audio_sha256
            st.mark_done("transcribed")
        state.save(st)
    return 0


def cmd_status(args) -> int:
    states = state.all_states()
    if not states:
        print("No pipeline state yet -- run 'fetch' first.")
        return 0
    by_stage = {s: 0 for s in state.STAGES}
    for st in states:
        for stage in st.completed_stages:
            by_stage[stage] = by_stage.get(stage, 0) + 1
    print(f"{len(states)} videos tracked\n")
    for stage in state.STAGES:
        print(f"  {stage}: {by_stage.get(stage, 0)}/{len(states)}")
    errors = [s for s in states if s.error]
    if errors:
        print(f"\n{len(errors)} videos with errors:")
        for s in errors:
            print(f"  {s.file_id} ({s.title}): {s.error}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Physics lecture notes pipeline")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("discover", help="List all lecture files from the manifest")
    p.set_defaults(func=cmd_discover)

    for name, fn, help_text in [
        ("fetch", cmd_fetch, "Download video(s) from Drive"),
        ("audio", cmd_audio, "Extract audio from fetched video(s)"),
    ]:
        p = sub.add_parser(name, help=help_text)
        p.add_argument("file_id", nargs="?", help="Drive file id (omit with --all)")
        p.add_argument("--all", action="store_true", help="Process every file in the manifest")
        p.set_defaults(func=fn)

    p = sub.add_parser("frames", help="Extract + dedupe board frames")
    p.add_argument("file_id", nargs="?", help="Drive file id (omit with --all)")
    p.add_argument("--all", action="store_true", help="Process every file in the manifest")
    p.add_argument(
        "--scene-detect", action="store_true", default=False,
        help="Also run ffmpeg scene-change detection. Off by default: verified "
             "against this library's real footage (screen-recorded stylus ink, "
             "not a camera on a board) to add zero frames while costing roughly "
             "half the extraction time -- see media.py's extract_scene_frames "
             "docstring. Worth re-enabling only for footage that's an actual "
             "camera recording with real scene cuts.",
    )
    p.set_defaults(func=cmd_frames)

    p = sub.add_parser("transcribe", help="Transcribe audio via Gemini")
    p.add_argument("file_id", nargs="?")
    p.add_argument("--all", action="store_true")
    p.add_argument("--force", action="store_true", help="Re-transcribe even if already done")
    p.set_defaults(func=cmd_transcribe)

    p = sub.add_parser("status", help="Show pipeline progress across all tracked videos")
    p.set_defaults(func=cmd_status)

    args = parser.parse_args()
    if getattr(args, "all", False) and getattr(args, "file_id", None):
        parser.error("pass either a file_id or --all, not both")
    if args.command in ("fetch", "audio", "frames", "transcribe") and not args.all and not args.file_id:
        parser.error("pass a file_id or --all")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
