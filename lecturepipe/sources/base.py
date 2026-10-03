"""Common interface every media source (Drive, yt-dlp, local disk)
implements, so the rest of the pipeline never branches on source type."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Protocol


@dataclass
class MediaRef:
    id: str
    title: str
    chapter_id: str
    size_bytes: int
    mime_type: str = "video/x-matroska"
    known_duplicate_of: str | None = None


class Source(Protocol):
    def list(self) -> Iterable[MediaRef]:
        """Enumerate every media item this source can provide."""
        ...

    def fetch(self, ref: MediaRef, dest_path: Path) -> None:
        """Download ref to dest_path. Must be resumable: if dest_path
        already has partial bytes, continue rather than restart."""
        ...
