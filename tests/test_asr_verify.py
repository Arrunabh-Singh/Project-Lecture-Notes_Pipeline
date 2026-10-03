import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lecturepipe.asr.gemini import Transcript, TranscriptSegment, build_prompt
from lecturepipe.asr.verify import check_coverage, chunk_boundaries, sanitize_segments


def _seg(start, end, text=None, conf="high"):
    # Unique-by-default text: an accidental shared default (e.g. "hello"
    # for every segment) would itself trigger the repetition-loop detector
    # and silently truncate test fixtures -- happened once already here.
    if text is None:
        text = f"segment at {start}"
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


def test_sanitize_drops_fabricated_content_past_true_duration():
    """Mirrors a real failure: gemini-3.5-flash-lite generated ~6 more
    minutes of coherent, non-repeating, plausible-sounding physics content
    past a verified-exact 1897.53s true duration on a real lecture. Audio
    cannot contain content past its measured duration -- this is a hard
    constraint, so anything past it must be dropped regardless of how
    genuine the text reads."""
    segs = [_seg(0, 30), _seg(30, 598), _seg(598, 605), _seg(650, 700), _seg(710, 750)]
    result = sanitize_segments(segs, true_duration_seconds=600.0)
    assert result.dropped_past_duration == 2  # the 650-700 and 710-750 segments
    assert len(result.segments) == 3
    assert result.segments[-1].end_seconds == 605


def test_sanitize_keeps_small_tail_within_grace():
    # DURATION_GRACE_SECONDS is an absolute 5s, not a percentage -- a
    # segment starting at 603s (within 5s of a 600s true duration) should
    # survive; one starting at 607s (beyond it) should not. Checked on
    # start_seconds, since that's what sanitize_segments actually filters.
    segs = [_seg(0, 30), _seg(30, 598), _seg(598, 603)]
    result = sanitize_segments(segs, true_duration_seconds=600.0)
    assert result.dropped_past_duration == 0
    assert len(result.segments) == 3


def test_sanitize_uses_absolute_not_percentage_grace():
    """Mirrors a real bug: DURATION_GRACE was originally a 3% multiplier,
    which is a 70-SECOND window on a real 2335.17s lecture -- large enough
    that a genuinely fabricated segment (starting 55s past the true
    duration, paraphrased rather than verbatim so the repetition detector
    also missed it) passed the old check untouched. An absolute grace
    catches it regardless of lecture length."""
    segs = [_seg(0, 2335), _seg(2335, 2390, text="a"), _seg(2390.7, 2420.7, text="b, worded differently")]
    result = sanitize_segments(segs, true_duration_seconds=2335.17)
    assert result.dropped_past_duration == 1
    assert len(result.segments) == 2


def test_sanitize_detects_repetition_loop():
    """Mirrors the worse real failure: the same sentence repeated
    verbatim with fabricated ever-increasing timestamps (1714% "coverage"
    on the raw, unsanitized transcript)."""
    loop_text = "So, you will have V_A - V_B = E_1 - ir_1, this is your equation one"
    segs = [
        _seg(0, 30, text="real content one"),
        _seg(30, 60, text="real content two"),
        _seg(60, 460, text=loop_text),
        _seg(460, 860, text=loop_text),
        _seg(860, 1260, text=loop_text),
    ]
    result = sanitize_segments(segs, true_duration_seconds=90.0)
    assert result.repetition_detected
    # keeps the first loop occurrence, drops the repeats
    assert len(result.segments) == 3
    assert result.segments[-1].text == loop_text


def test_check_coverage_uses_sanitized_segments_not_raw():
    """The exact bug found live: raw coverage read 1714% because it
    trusted fabricated timestamps. Coverage must be computed on sanitized
    segments, or the metric actively hides the failure it exists to catch."""
    loop_text = "repeated fabricated sentence"
    segs = [
        _seg(0, 30, text="real"),
        _seg(30, 598, text="also real"),
        _seg(598, 1000, text=loop_text),
        _seg(1000, 2000, text=loop_text),
    ]
    t = Transcript(segments=segs, source_audio_sha256="deadbeef")
    result = check_coverage(t, true_duration_seconds=600.0)
    assert result.coverage_ratio < 2.0  # not the ~333% the raw last-timestamp would give
    assert result.passed  # 598/600 is within COVERAGE_THRESHOLD
    assert result.sanitize.repetition_detected


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
