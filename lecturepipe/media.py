"""ffmpeg wrapper for audio extraction and board-frame extraction.

Uses imageio_ffmpeg's bundled static binary rather than a system package,
because apt (deb.debian.org) is blocked by this environment's network
policy but PyPI wheels are reachable.
"""
from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

# ffprobe isn't bundled by imageio-ffmpeg, but ffmpeg itself can report
# duration via -i on a nonexistent output; simplest robust path is to
# invoke ffmpeg with no output and parse stderr, which works with the same
# single binary and needs no extra download.
DURATION_RE = re.compile(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)")


class MediaError(RuntimeError):
    pass


def probe_duration_seconds(video_path: Path) -> float:
    proc = subprocess.run(
        [FFMPEG, "-i", str(video_path)],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    m = DURATION_RE.search(proc.stderr)
    if not m:
        raise MediaError(f"Could not determine duration for {video_path}:\n{proc.stderr[-500:]}")
    h, mnt, s = m.groups()
    return int(h) * 3600 + int(mnt) * 60 + float(s)


def slice_audio(audio_path: Path, out_path: Path, start_seconds: float, end_seconds: float) -> Path:
    """Extract [start, end) from an existing WAV, for the chunk-fallback
    path when a single-shot transcription under-covers a lecture (~25% of
    this library's lectures on gemini-3.5-flash-lite, seen live). -ss
    before -i for fast seek; re-encoding (not stream copy) since a PCM WAV
    has no keyframe-alignment concept to worry about, so an exact cut is
    cheap either way."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        FFMPEG, "-y",
        "-ss", str(start_seconds), "-to", str(end_seconds),
        "-i", str(audio_path),
        "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le",
        str(out_path),
    ]
    proc = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    if proc.returncode != 0 or not out_path.exists():
        raise MediaError(f"Audio slicing failed for {audio_path} [{start_seconds}-{end_seconds}]:\n{proc.stderr[-800:]}")
    return out_path


def extract_audio(video_path: Path, out_path: Path, sample_rate: int = 16000) -> Path:
    """Mono 16kHz WAV -- small enough for Gemini's Files API, and 16kHz is
    plenty for speech (well above the ~8kHz Nyquist needed for intelligible
    voice, matching what most ASR front-ends resample to internally)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        FFMPEG, "-y", "-i", str(video_path),
        "-vn", "-ac", "1", "-ar", str(sample_rate),
        "-c:a", "pcm_s16le",
        str(out_path),
    ]
    proc = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    if proc.returncode != 0 or not out_path.exists():
        raise MediaError(f"Audio extraction failed for {video_path}:\n{proc.stderr[-800:]}")
    return out_path


@dataclass
class FrameSpec:
    timestamp_seconds: float
    path: Path


def extract_scene_frames(
    video_path: Path,
    out_dir: Path,
    scene_threshold: float = 0.35,
    coverage_floor_seconds: float = 20.0,
    duration_seconds: float | None = None,
    enable_scene_detect: bool = True,
) -> list[FrameSpec]:
    """Two extraction passes merged together:

    1. Scene-change detection (ffmpeg's `select='gt(scene,threshold)'`) --
       catches the moment the board content actually changes. USELESS on
       this library's actual footage: these lectures are screen recordings
       of stylus ink on a static Microsoft Word page, not a camera on a
       physical board. Scene score measures frame-to-frame pixel delta,
       and one ink stroke's delta is ~0.0001-0.0003 -- three orders of
       magnitude below the 0.35 default. Verified empirically (ffmpeg
       metadata=print across a real 42-minute lecture, zero frames past
       threshold) before dropping the default coverage-floor interval to
       compensate, rather than assumed. Left enabled (not removed) since a
       genuinely camera-filmed board elsewhere in this project would make
       it useful again -- it's dead weight for THIS library, not universally.
    2. A fixed-interval "coverage floor" every `coverage_floor_seconds` --
       catches long static stretches (a teacher talking through one board
       for 3 minutes) that scene-detect alone would skip entirely.
       Borrowed from claude-watch's coverage-floor idea (see plan's prior
       art section) rather than reinvented from scratch. Default tightened
       from 45s to 20s given (1) above -- this is now the only real signal,
       and perceptual-hash dedupe (frames.py, already verified to collapse
       true near-duplicates) keeps the denser sampling from blowing up
       frame counts.

    Frames from both passes land in the same directory with timestamp-
    encoded filenames; perceptual-hash dedupe (frames.py) removes the
    overlap between the two passes downstream.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    frames: list[FrameSpec] = []

    if enable_scene_detect:
        scene_pattern = str(out_dir / "scene_%06d.jpg")
        cmd_scene = [
            FFMPEG, "-y", "-i", str(video_path),
            "-vf", f"select='gt(scene,{scene_threshold})',showinfo",
            "-vsync", "vfr",
            "-q:v", "3",
            scene_pattern,
        ]
        proc = subprocess.run(cmd_scene, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        if proc.returncode != 0:
            raise MediaError(f"Scene-detect frame extraction failed for {video_path}:\n{proc.stderr[-800:]}")

        scene_timestamps = [float(t) for t in re.findall(r"pts_time:(\d+\.?\d*)", proc.stderr)]
        scene_files = sorted(out_dir.glob("scene_*.jpg"))
        frames.extend(
            FrameSpec(timestamp_seconds=ts, path=p)
            for ts, p in zip(scene_timestamps, scene_files)
        )

    if duration_seconds:
        floor_pattern = str(out_dir / "floor_%06d.jpg")
        cmd_floor = [
            FFMPEG, "-y", "-i", str(video_path),
            "-vf", f"fps=1/{coverage_floor_seconds}",
            "-q:v", "3",
            floor_pattern,
        ]
        proc2 = subprocess.run(cmd_floor, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        if proc2.returncode != 0:
            raise MediaError(f"Coverage-floor frame extraction failed for {video_path}:\n{proc2.stderr[-800:]}")
        floor_files = sorted(out_dir.glob("floor_*.jpg"))
        for i, p in enumerate(floor_files):
            frames.append(FrameSpec(timestamp_seconds=i * coverage_floor_seconds, path=p))

    frames.sort(key=lambda f: f.timestamp_seconds)
    return frames
