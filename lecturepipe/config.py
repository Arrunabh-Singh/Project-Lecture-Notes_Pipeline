"""Environment and path configuration. Loads .env manually (no python-dotenv
dependency) so `.env` values are available via os.environ without requiring
the caller to `source` anything first."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
LECTURES_DIR = DATA_DIR / "lectures"      # gitignored: video/audio/frames
CACHE_DIR = DATA_DIR / "cache"            # gitignored: ASR response cache
NCERT_DIR = DATA_DIR / "ncert" / "processed"
MANIFEST_PATH = DATA_DIR / "lecture_manifest.json"
NOTES_DIR = ROOT / "notes"
STATE_DIR = ROOT / "state"
PUBLISH_DIR = DATA_DIR / "publish"        # gitignored: generated HTML build output


def _load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        if key and key not in os.environ:
            os.environ[key] = value


_load_dotenv(ROOT / ".env")


class Config:
    drive_access_token: str | None = os.environ.get("DRIVE_ACCESS_TOKEN") or None
    drive_refresh_token: str | None = os.environ.get("DRIVE_REFRESH_TOKEN") or None
    drive_client_id: str | None = os.environ.get("DRIVE_CLIENT_ID") or None
    drive_client_secret: str | None = os.environ.get("DRIVE_CLIENT_SECRET") or None

    gemini_api_key: str | None = os.environ.get("GEMINI_API_KEY") or None
    gemini_model: str = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash")
    gemini_rate_limit_rpm: int = int(os.environ.get("GEMINI_RATE_LIMIT_RPM", "6"))

    @property
    def has_drive_credentials(self) -> bool:
        return bool(self.drive_access_token or self.drive_refresh_token)

    @property
    def has_gemini_credentials(self) -> bool:
        return bool(self.gemini_api_key)


config = Config()

for _dir in (LECTURES_DIR, CACHE_DIR, NOTES_DIR, STATE_DIR, PUBLISH_DIR):
    _dir.mkdir(parents=True, exist_ok=True)
