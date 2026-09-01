"""Coverage validation and transcript sanitization.

Two distinct long-audio ASR failure modes, found live against real lecture
audio, not hypothesized:

1. Silent truncation -- the model stops transcribing partway through and
   the response just ends, with no error. Caught by comparing the
   transcript's last timestamp against the audio's real duration.
2. Post-duration fabrication -- worse, and NOT caught by (1)'s naive
   coverage check, because it makes coverage look too GOOD, not too bad.
   Seen live on a real 31m 37.53s lecture (verified via ffprobe on both the
   source video and the extracted WAV, and independently via raw
   file-size arithmetic -- all three agree exactly, so this is a hard
   ground truth, not a heuristic): gemini-3.5-flash-lite kept generating
   segments for another ~6 minutes past the true end, at least once
   degenerating into a verbatim repeated sentence with fabricated
   ever-increasing timestamps (1714% "coverage"), but on a different file
   the extra material was coherent, plausible, non-repeating physics
   content indistinguishable from real lecture material by reading alone.
   Since audio cannot contain content past its measured duration, ANY
   segment starting past that boundary is fabricated by definition --
   this is a hard physical constraint, not a confidence threshold. Trust
   nothing past it, regardless of how genuine it reads.
"""
from __future__ import annotations

from dataclasses import dataclass

from lecturepipe.asr.gemini import Transcript, TranscriptSegment

# If the transcript covers less than this fraction of the true duration,
# treat it as truncated rather than "the lecture happened to end in silence".
COVERAGE_THRESHOLD = 0.92

# Small ABSOLUTE grace for trivial timestamp rounding at the very tail --
# NOT a tolerance for genuine overshoot, since true_duration_seconds is
# verified ground truth (see module docstring). Deliberately a constant,
# not a percentage: a multiplicative 3% margin (the original design) gives
# a 70-SECOND window on a 40-minute lecture, and a real fabricated segment
# was found live hiding inside exactly that window -- paraphrased, not
# verbatim, so the repetition detector missed it too (see
# test_sanitize_drops_near_duplicate_paraphrase_past_grace). "Trivial
# rounding" is a roughly constant few-second effect regardless of lecture
# length; it should not get more forgiving on longer lectures, which is
# backwards -- longer lectures are exactly where there's more room for
# fabrication to hide.
DURATION_GRACE_SECONDS = 5.0


@dataclass
class SanitizeResult:
    segments: list[TranscriptSegment]
    dropped_past_duration: int
    dropped_repetition: int
    repetition_detected: bool


def _normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())


def sanitize_segments(segments: list[TranscriptSegment], true_duration_seconds: float) -> SanitizeResult:
    """Strip fabricated tail content: anything past the verified true
    duration, and any run of repeated text -- exact OR near-duplicate
    (normalized: lowercased, whitespace-collapsed), since a real
    fabrication loop was found paraphrasing itself slightly each repeat
    rather than repeating verbatim. Once either failure mode is detected,
    everything from that point onward is dropped, not just the segments
    that individually fail the check -- once a model has started
    fabricating, nothing after that point in the same response should be
    trusted, even if a later segment happens to look fine in isolation.
    """
    max_trustworthy = true_duration_seconds + DURATION_GRACE_SECONDS

    # First index whose start is past the trustworthy boundary -- a hard
    # physical cutoff, checked independently of repetition.
    duration_cutoff = next(
        (i for i, s in enumerate(segments) if s.start_seconds > max_trustworthy), None
    )
    # First index that repeats the previous segment (normalized match) --
    # the loop-detection failure mode, independent of duration.
    repetition_cutoff = next(
        (i + 1 for i in range(len(segments) - 1)
         if _normalize(segments[i].text) and _normalize(segments[i].text) == _normalize(segments[i + 1].text)),
        None,
    )

    candidates = [c for c in (duration_cutoff, repetition_cutoff) if c is not None]
    cutoff = min(candidates) if candidates else None
    repetition_detected = repetition_cutoff is not None and cutoff == repetition_cutoff

    kept = segments[:cutoff] if cutoff is not None else list(segments)
    dropped_total = len(segments) - len(kept)
    dropped_repetition = dropped_total if repetition_detected else 0
    dropped_past_duration = 0 if repetition_detected else dropped_total

    return SanitizeResult(
        segments=kept,
        dropped_past_duration=dropped_past_duration,
        dropped_repetition=dropped_repetition,
        repetition_detected=repetition_detected,
    )


@dataclass
class CoverageResult:
    covered_seconds: float
    true_duration_seconds: float
    coverage_ratio: float
    passed: bool
    low_confidence_count: int
    sanitize: SanitizeResult | None = None

    @property
    def needs_chunk_fallback(self) -> bool:
        return not self.passed


def check_coverage(transcript: Transcript, true_duration_seconds: float) -> CoverageResult:
    """Sanitizes first, then computes coverage against the cleaned
    segments -- coverage on raw (unsanitized) segments is actively
    misleading for failure mode 2 above: fabricated tail content makes
    coverage look artificially high, hiding the exact problem this check
    exists to catch."""
    result = sanitize_segments(transcript.segments, true_duration_seconds)
    covered = result.segments[-1].end_seconds if result.segments else 0.0
    ratio = covered / true_duration_seconds if true_duration_seconds > 0 else 0.0
    low_conf = sum(1 for s in result.segments if s.confidence == "low")
    return CoverageResult(
        covered_seconds=covered,
        true_duration_seconds=true_duration_seconds,
        coverage_ratio=ratio,
        passed=ratio >= COVERAGE_THRESHOLD,
        low_confidence_count=low_conf,
        sanitize=result,
    )


def chunk_boundaries(true_duration_seconds: float, chunk_seconds: float = 600.0) -> list[tuple[float, float]]:
    """10-minute chunk boundaries for the fallback path, used only when a
    single-shot transcription under-covers the audio (see plan's budget
    section: single-shot is the default, chunking is the exception)."""
    boundaries = []
    t = 0.0
    while t < true_duration_seconds:
        end = min(t + chunk_seconds, true_duration_seconds)
        boundaries.append((t, end))
        t = end
    return boundaries
