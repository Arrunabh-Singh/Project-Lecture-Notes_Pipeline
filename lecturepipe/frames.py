"""Perceptual-hash dedupe for the merged scene-detect + coverage-floor frame
set from media.py. The two extraction passes overlap by design (a scene
change that happens to land near a coverage-floor tick), so this collapses
near-duplicate frames before they reach the notes-synthesis step, where
each frame costs a Read-tool call."""
from __future__ import annotations

from dataclasses import dataclass

import imagehash
from PIL import Image

from lecturepipe.media import FrameSpec

# Hamming distance below which two frames are considered the same board
# state. 64-bit phash; a handful of bits of difference is JPEG noise, not
# a real content change.
DEDUPE_THRESHOLD = 6


@dataclass
class DedupedFrame:
    timestamp_seconds: float
    path: str
    phash: str


def dedupe_frames(frames: list[FrameSpec]) -> list[DedupedFrame]:
    ordered = sorted(frames, key=lambda f: f.timestamp_seconds)
    kept: list[DedupedFrame] = []
    for f in ordered:
        try:
            h = imagehash.phash(Image.open(f.path))
        except Exception:
            continue  # corrupt/unreadable frame -- skip rather than crash a 59-video batch
        if kept and (h - imagehash.hex_to_hash(kept[-1].phash)) <= DEDUPE_THRESHOLD:
            continue  # near-duplicate of the immediately preceding kept frame
        kept.append(DedupedFrame(timestamp_seconds=f.timestamp_seconds, path=str(f.path), phash=str(h)))
    return kept
