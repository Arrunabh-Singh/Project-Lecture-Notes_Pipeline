"""Per-video checkpoint state, persisted as JSON so any pipeline stage can
resume after the container is reclaimed mid-run. Each video's state lives
in its own file, keyed by Drive file id -- never one giant state blob that
a crash mid-write could corrupt for all 59 videos at once."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from lecturepipe.config import STATE_DIR

STAGES = (
    "fetched",
    "audio_extracted",
    "frames_extracted",
    "transcribed",
    "notes_written",
    "published",
)


@dataclass
class VideoState:
    file_id: str
    chapter_id: str
    title: str
    completed_stages: list[str] = field(default_factory=list)
    sha256: str | None = None
    duration_seconds: float | None = None
    transcript_cache_key: str | None = None
    frame_count: int | None = None
    error: str | None = None

    def is_done(self, stage: str) -> bool:
        return stage in self.completed_stages

    def mark_done(self, stage: str) -> None:
        if stage not in self.completed_stages:
            self.completed_stages.append(stage)
        self.error = None

    def mark_error(self, message: str) -> None:
        self.error = message


def _path(file_id: str) -> Path:
    return STATE_DIR / f"{file_id}.json"


def load(file_id: str, chapter_id: str = "", title: str = "") -> VideoState:
    p = _path(file_id)
    if p.exists():
        data: dict[str, Any] = json.loads(p.read_text())
        return VideoState(**data)
    return VideoState(file_id=file_id, chapter_id=chapter_id, title=title)


def save(state: VideoState) -> None:
    _path(state.file_id).write_text(json.dumps(asdict(state), indent=2))


def all_states() -> list[VideoState]:
    out = []
    for p in sorted(STATE_DIR.glob("*.json")):
        out.append(VideoState(**json.loads(p.read_text())))
    return out
