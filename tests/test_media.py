"""Tests for media.py against real ffmpeg output (not mocked -- ffmpeg is
a real dependency, and its actual behavior is what matters here)."""
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lecturepipe.media import extract_audio, extract_scene_frames, probe_duration_seconds

FFMPEG_BIN = None


def _make_test_video(path: Path, duration: int = 9) -> None:
    """3 concatenated 3s segments of distinct textured patterns -- solid
    colors don't work here: phash finds no structure in a flat color and
    collapses all of them together, which isn't representative of real
    board/frame content. See git history for that finding."""
    import imageio_ffmpeg
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    import subprocess
    cmd = [
        ffmpeg, "-y",
        "-f", "lavfi", "-i", "testsrc=s=320x240:d=3",
        "-f", "lavfi", "-i", "testsrc2=s=320x240:d=3",
        "-f", "lavfi", "-i", "smptebars=s=320x240:d=3",
        "-f", "lavfi", "-i", f"sine=frequency=440:duration={duration}",
        "-filter_complex", "[0:v][1:v][2:v]concat=n=3:v=1:a=0[v]",
        "-map", "[v]", "-map", "3:a", "-c:v", "libx264", "-c:a", "aac", str(path),
    ]
    subprocess.run(cmd, capture_output=True, check=True)


def test_probe_duration_matches_generated_video():
    with tempfile.TemporaryDirectory() as tmp:
        video = Path(tmp) / "test.mp4"
        _make_test_video(video)
        duration = probe_duration_seconds(video)
        assert abs(duration - 9.0) < 0.5


def test_extract_audio_produces_valid_wav():
    with tempfile.TemporaryDirectory() as tmp:
        video = Path(tmp) / "test.mp4"
        _make_test_video(video)
        audio = extract_audio(video, Path(tmp) / "audio.wav")
        assert audio.exists()
        assert audio.stat().st_size > 0


def test_frames_extracted_with_scene_detect_disabled():
    """This library's real footage (screen-recorded stylus ink) makes
    scene-detect useless -- verified against real lecture video: zero
    frames past threshold, near-zero scene scores throughout. Coverage-
    floor alone must still produce a sensible frame count."""
    with tempfile.TemporaryDirectory() as tmp:
        video = Path(tmp) / "test.mp4"
        _make_test_video(video)
        frames = extract_scene_frames(
            video, Path(tmp) / "frames",
            duration_seconds=9.0, coverage_floor_seconds=2.0,
            enable_scene_detect=False,
        )
        assert len(frames) >= 3  # 9s / 2s floor interval
        assert all(f.path.exists() for f in frames)
        assert all("scene_" not in f.path.name for f in frames)


def test_frames_extracted_with_scene_detect_enabled():
    """Scene-detect path must still work for footage where it IS useful
    (an actual camera on a board) -- this default stays available even
    though the CLI now defaults it off for this specific library."""
    with tempfile.TemporaryDirectory() as tmp:
        video = Path(tmp) / "test.mp4"
        _make_test_video(video)
        frames = extract_scene_frames(
            video, Path(tmp) / "frames",
            duration_seconds=9.0, coverage_floor_seconds=2.0,
            enable_scene_detect=True,
        )
        scene_frames = [f for f in frames if "scene_" in f.path.name]
        # testsrc/testsrc2/smptebars are visually distinct enough that
        # scene-detect should catch at least the 2 hard transitions between them
        assert len(scene_frames) >= 1


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
        except Exception as e:
            failed += 1
            print(f"FAIL {t.__name__}: {e}")
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
