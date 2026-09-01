"""Coverage validation: the main failure mode of single-shot long-audio ASR
is silent truncation (the model stops transcribing partway through and the
response just... ends, with no error). Comparing the transcript's last
timestamp against the audio's real duration catches this reliably."""
from __future__ import annotations

from dataclasses import dataclass

from lecturepipe.asr.gemini import Transcript

# If the transcript covers less than this fraction of the true duration,
# treat it as truncated rather than "the lecture happened to end in silence".
COVERAGE_THRESHOLD = 0.92


@dataclass
class CoverageResult:
    covered_seconds: float
    true_duration_seconds: float
    coverage_ratio: float
    passed: bool
    low_confidence_count: int

    @property
    def needs_chunk_fallback(self) -> bool:
        return not self.passed


def check_coverage(transcript: Transcript, true_duration_seconds: float) -> CoverageResult:
    covered = transcript.covered_seconds
    ratio = covered / true_duration_seconds if true_duration_seconds > 0 else 0.0
    return CoverageResult(
        covered_seconds=covered,
        true_duration_seconds=true_duration_seconds,
        coverage_ratio=ratio,
        passed=ratio >= COVERAGE_THRESHOLD,
        low_confidence_count=len(transcript.low_confidence_segments),
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
