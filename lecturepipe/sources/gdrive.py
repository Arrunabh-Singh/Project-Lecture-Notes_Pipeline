"""Google Drive source: downloads lecture videos over the Drive v3 REST API
directly (www.googleapis.com), NOT through the Drive MCP connector.

Why not the connector: its download_file_content tool returns file bytes as
inline base64 in the tool result. For a 25MB video that's roughly 33MB of
base64 -- millions of tokens -- landing in the agent's context window.
Verified experimentally against this library before this module was
written. The connector is used elsewhere in this pipeline for NCERT PDF
text and for Drive metadata/listing, both of which are small; it is never
used for video bytes.

This module instead authenticates directly against the Drive REST API and
streams to disk with resumable HTTP Range requests, so a token expiring or
a connection dropping mid-download loses at most the current chunk, not the
whole file.
"""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Iterable

import requests

from lecturepipe.config import MANIFEST_PATH, config
from lecturepipe.sources.base import MediaRef

DRIVE_API = "https://www.googleapis.com/drive/v3"
TOKEN_URL = "https://oauth2.googleapis.com/token"
CHUNK_SIZE = 1024 * 1024  # 1 MiB
MAX_RETRIES = 5


class DriveAuthError(RuntimeError):
    """Raised when no usable credential is configured, or a token is
    expired and cannot be refreshed. Message is written to guide the user
    to the fix rather than just stating the failure."""


class DriveTokenManager:
    """Wraps whichever credential shape the user provided: a bare access
    token (simplest, expires in ~1h, no auto-refresh possible), or a full
    refresh-token trio (auto-refreshes indefinitely)."""

    def __init__(self) -> None:
        self._access_token = config.drive_access_token
        self._expiry = 0.0  # unix time; 0 means "unknown/assume valid"
        if not config.has_drive_credentials:
            raise DriveAuthError(
                "No Drive credentials configured. Set DRIVE_ACCESS_TOKEN "
                "(from https://developers.google.com/oauthplayground, "
                "drive.readonly scope) in .env, or the DRIVE_REFRESH_TOKEN "
                "/ DRIVE_CLIENT_ID / DRIVE_CLIENT_SECRET trio for auto-refresh."
            )

    def get_token(self) -> str:
        if self._access_token and time.time() < self._expiry - 30:
            return self._access_token
        if self._access_token and not config.drive_refresh_token:
            # Bare access token, no way to refresh -- hand back what we
            # have and let the caller discover expiry from a 401, since we
            # have no expiry timestamp for a token we didn't mint ourselves.
            return self._access_token
        if config.drive_refresh_token:
            self._refresh()
            return self._access_token  # type: ignore[return-value]
        raise DriveAuthError("Drive access token missing or expired, and no refresh token configured.")

    def _refresh(self) -> None:
        resp = requests.post(
            TOKEN_URL,
            data={
                "client_id": config.drive_client_id,
                "client_secret": config.drive_client_secret,
                "refresh_token": config.drive_refresh_token,
                "grant_type": "refresh_token",
            },
            timeout=30,
        )
        if resp.status_code != 200:
            raise DriveAuthError(f"Drive token refresh failed: {resp.status_code} {resp.text[:300]}")
        payload = resp.json()
        self._access_token = payload["access_token"]
        self._expiry = time.time() + payload.get("expires_in", 3600)


class DriveSource:
    def __init__(self, manifest_path: Path = MANIFEST_PATH) -> None:
        self._manifest_path = manifest_path
        self._tokens: DriveTokenManager | None = None  # lazy: list() needs no credentials

    @property
    def tokens(self) -> DriveTokenManager:
        if self._tokens is None:
            self._tokens = DriveTokenManager()
        return self._tokens

    def list(self) -> Iterable[MediaRef]:
        manifest = json.loads(self._manifest_path.read_text())
        for chapter in manifest["chapters"]:
            for f in chapter["files"]:
                yield MediaRef(
                    id=f["id"],
                    title=f["title"],
                    chapter_id=chapter["chapter_id"],
                    size_bytes=f["size_bytes"],
                    mime_type=f.get("mime_type", "video/x-matroska"),
                    known_duplicate_of=f.get("known_duplicate_of"),
                )

    def fetch(self, ref: MediaRef, dest_path: Path) -> None:
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = dest_path.with_suffix(dest_path.suffix + ".part")

        resume_from = tmp_path.stat().st_size if tmp_path.exists() else 0
        if dest_path.exists() and dest_path.stat().st_size == ref.size_bytes:
            return  # already fully fetched in a previous run

        url = f"{DRIVE_API}/files/{ref.id}?alt=media"
        attempt = 0
        while True:
            attempt += 1
            headers = {"Authorization": f"Bearer {self.tokens.get_token()}"}
            if resume_from:
                headers["Range"] = f"bytes={resume_from}-"
            try:
                with requests.get(url, headers=headers, stream=True, timeout=60) as resp:
                    if resp.status_code == 401:
                        raise DriveAuthError(
                            "Drive returned 401 (token expired/invalid). "
                            "Generate a fresh access token and update .env, then re-run -- "
                            "download will resume from the last byte written, not restart."
                        )
                    if resp.status_code not in (200, 206):
                        raise RuntimeError(f"Drive download failed for {ref.id}: HTTP {resp.status_code} {resp.text[:200]}")
                    mode = "ab" if resume_from and resp.status_code == 206 else "wb"
                    if mode == "wb":
                        resume_from = 0
                    with open(tmp_path, mode) as fh:
                        for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
                            if chunk:
                                fh.write(chunk)
                                resume_from += len(chunk)
                break
            except (requests.exceptions.RequestException,) as exc:
                if attempt >= MAX_RETRIES:
                    raise RuntimeError(f"Drive download failed after {MAX_RETRIES} attempts for {ref.id}: {exc}") from exc
                resume_from = tmp_path.stat().st_size if tmp_path.exists() else 0
                time.sleep(min(2 ** attempt, 30))

        final_size = tmp_path.stat().st_size
        if final_size != ref.size_bytes:
            raise RuntimeError(
                f"Downloaded size mismatch for {ref.id} ({ref.title}): "
                f"got {final_size} bytes, manifest says {ref.size_bytes}. "
                "Not renaming to final path -- re-run to resume/retry."
            )
        tmp_path.rename(dest_path)

    @staticmethod
    def sha256_of(path: Path) -> str:
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(CHUNK_SIZE), b""):
                h.update(chunk)
        return h.hexdigest()
