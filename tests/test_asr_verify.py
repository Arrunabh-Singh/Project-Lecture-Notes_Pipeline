import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lecturepipe.asr.gemini import Transcript, TranscriptSegment, build_prompt
from lecturepipe.asr.verify import check_coverage, chunk_boundaries


def _seg(start, end, text="hello", conf="high"):
    return TranscriptSegment(start_seconds=start, end_seconds=end, text=text, confidence=conf)


def test_coverage_pass_full_lecture():
    segs = [_seg(0, 30), _seg(30, 60), _seg(60, 598)]
    t = Transcript(segments=segs, source_audio_sha256="deadbeef")
    result = check_coverage(t, true_duration_seconds=600.0)
    assert result.passed
    assert result.coverage_ratio > 0.99
    assert not result.needs_chunk_fallback


def test_coverage_fail_truncated():
    segs = [_seg(0, 30), _seg(30, 60)]  # transcript stops at 60s of a 600s lecture
    t = Transcript(segments=segs, source_audio_sha256="deadbeef")
    result = check_coverage(t, true_duration_seconds=600.0)
    assert not result.passed
    assert result.needs_chunk_fallback
    assert result.coverage_ratio == 0.1


def test_coverage_empty_transcript():
    t = Transcript(segments=[], source_audio_sha256="deadbeef")
    result = check_coverage(t, true_duration_seconds=600.0)
    assert not result.passed
    assert result.coverage_ratio == 0.0


def test_low_confidence_counted():
    segs = [_seg(0, 30, conf="low"), _seg(30, 598, conf="high"), _seg(598, 599, conf="low")]
    t = Transcript(segments=segs, source_audio_sha256="deadbeef")
    result = check_coverage(t, true_duration_seconds=600.0)
    assert result.low_confidence_count == 2
    assert len(t.low_confidence_segments) == 2


def test_chunk_boundaries_exact_division():
    b = chunk_boundaries(1200.0, chunk_seconds=600.0)
    assert b == [(0.0, 600.0), (600.0, 1200.0)]


def test_chunk_boundaries_remainder():
    b = chunk_boundaries(1450.0, chunk_seconds=600.0)
    assert b == [(0.0, 600.0), (600.0, 1200.0), (1200.0, 1450.0)]
    # last chunk shouldn't overrun true duration
    assert b[-1][1] == 1450.0


def test_chunk_boundaries_short_lecture_single_chunk():
    b = chunk_boundaries(300.0, chunk_seconds=600.0)
    assert b == [(0.0, 300.0)]


def test_build_prompt_includes_lexicon_and_hinglish_rules():
    lexicon = ["Electric Field", "Coulomb", "Gauss Law"]
    prompt = build_prompt("Electric Charges and Fields", lexicon)
    assert "Hinglish" in prompt
    assert "Electric Field" in prompt
    assert "Devanagari" in prompt
    assert "verbatim" in prompt.lower()


def test_build_prompt_caps_lexicon_size():
    lexicon = [f"term{i}" for i in range(500)]
    prompt = build_prompt("Test Chapter", lexicon)
    # only first 120 terms should appear
    assert "term119" in prompt
    assert "term200" not in prompt


if __name__ == "__main__":
    import inspect
    mod = sys.modules[__name__]
    tests = [f for name, f in inspect.getmembers(mod) if name.startswith("test_")]
    passed = failed = 0
    for t in tests:
        try:
            t()
            passed += 1
            print(f"PASS {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL {t.__name__}: {e}")
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
