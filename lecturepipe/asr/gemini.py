"""Gemini-based ASR: one request per lecture (not per chunk -- see plan's
budget section), using the Files API for audio since a 40-minute lecture's
16kHz mono WAV (~77MB) is well over Gemini's ~20MB inline-request limit.

Structured JSON output (responseSchema) is used instead of free-text
parsing, since format drift in a 40-minute transcript is exactly the kind
of failure that's expensive to catch after the fact.
"""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass
from pathlib import Path

import requests

from lecturepipe.config import CACHE_DIR, config

API_BASE = "https://generativelanguage.googleapis.com"
UPLOAD_BASE = f"{API_BASE}/upload/v1beta/files"

# Prompt version is part of the cache key: bump this if the prompt changes
# so stale cached transcripts don't silently keep serving under a new
# prompt's semantics.
PROMPT_VERSION = "v1"

TRANSCRIPT_SCHEMA = {
    "type": "object",
    "properties": {
        "segments": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "start_seconds": {"type": "number"},
                    "end_seconds": {"type": "number"},
                    "text": {"type": "string"},
                    "confidence": {"type": "string", "enum": ["high", "low"]},
                },
                "required": ["start_seconds", "end_seconds", "text", "confidence"],
            },
        }
    },
    "required": ["segments"],
}


class GeminiAuthError(RuntimeError):
    pass


class GeminiASRError(RuntimeError):
    pass


@dataclass
class TranscriptSegment:
    start_seconds: float
    end_seconds: float
    text: str
    confidence: str  # "high" | "low"


@dataclass
class Transcript:
    segments: list[TranscriptSegment]
    source_audio_sha256: str
    cache_hit: bool = False

    @property
    def covered_seconds(self) -> float:
        return self.segments[-1].end_seconds if self.segments else 0.0

    @property
    def low_confidence_segments(self) -> list[TranscriptSegment]:
        return [s for s in self.segments if s.confidence == "low"]


def build_prompt(chapter_title: str, lexicon: list[str]) -> str:
    lexicon_str = ", ".join(lexicon[:120])  # cap prompt size; lexicon is already deduped/sorted
    return f"""Transcribe this physics lecture audio verbatim. The lecture is on
"{chapter_title}" (NCERT Class 12 Physics) and the speech is Hinglish
(code-switched Hindi/English), typical of an Indian classroom.

Rules:
- Transcribe EXACTLY what is spoken, in the language it was spoken. Do not
  translate Hindi to English or vice versa. Preserve code-switching mid-sentence
  exactly as spoken.
- Write Hindi words in Devanagari script, not English transliteration.
- These technical terms are likely to appear (from the NCERT chapter text) --
  use this list to resolve ambiguous audio, don't force terms that weren't said:
  {lexicon_str}
- Segment the transcript into short spans (a few seconds to ~20s each) with
  accurate start/end timestamps in seconds from the start of the audio.
- Mark confidence "low" on any segment where you are genuinely uncertain of
  the words (mumbling, crosstalk, inaudible audio, ambiguous jargon) --
  do not mark low confidence just because the content is technical.
- Cover the ENTIRE audio from 0 seconds to the end. Do not stop early or
  summarize a stretch as silence unless it truly is silence.
"""


def _cache_key(audio_sha256: str) -> str:
    return hashlib.sha256(f"{audio_sha256}:{PROMPT_VERSION}".encode()).hexdigest()


def _cache_path(audio_sha256: str) -> Path:
    return CACHE_DIR / f"transcript_{_cache_key(audio_sha256)}.json"


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


class RateLimiter:
    def __init__(self, rpm: int) -> None:
        self._min_interval = 60.0 / max(rpm, 1)
        self._last_call = 0.0

    def wait(self) -> None:
        elapsed = time.monotonic() - self._last_call
        if elapsed < self._min_interval:
            time.sleep(self._min_interval - elapsed)
        self._last_call = time.monotonic()


_rate_limiter = RateLimiter(config.gemini_rate_limit_rpm)


def _require_key() -> str:
    if not config.gemini_api_key:
        raise GeminiAuthError(
            "GEMINI_API_KEY not set. Get a free key (no card) at "
            "https://aistudio.google.com/apikey and add it to .env."
        )
    return config.gemini_api_key


def upload_audio(audio_path: Path, mime_type: str = "audio/wav") -> str:
    """Resumable upload via the Files API. Returns the file's URI, usable
    in a subsequent generateContent call as a file_data part."""
    key = _require_key()
    size = audio_path.stat().st_size

    start_resp = requests.post(
        f"{UPLOAD_BASE}?key={key}",
        headers={
            "X-Goog-Upload-Protocol": "resumable",
            "X-Goog-Upload-Command": "start",
            "X-Goog-Upload-Header-Content-Length": str(size),
            "X-Goog-Upload-Header-Content-Type": mime_type,
            "Content-Type": "application/json",
        },
        json={"file": {"display_name": audio_path.name}},
        timeout=30,
    )
    if start_resp.status_code == 401 or start_resp.status_code == 403:
        raise GeminiAuthError(f"Gemini upload auth failed: {start_resp.status_code} {start_resp.text[:300]}")
    if start_resp.status_code != 200:
        raise GeminiASRError(f"Gemini upload start failed: {start_resp.status_code} {start_resp.text[:300]}")
    upload_url = start_resp.headers.get("X-Goog-Upload-URL")
    if not upload_url:
        raise GeminiASRError(f"Gemini upload start returned no upload URL: {start_resp.headers}")

    with open(audio_path, "rb") as fh:
        data = fh.read()
    finish_resp = requests.post(
        upload_url,
        headers={
            "X-Goog-Upload-Offset": "0",
            "X-Goog-Upload-Command": "upload, finalize",
        },
        data=data,
        timeout=300,
    )
    if finish_resp.status_code != 200:
        raise GeminiASRError(f"Gemini upload finalize failed: {finish_resp.status_code} {finish_resp.text[:300]}")
    file_info = finish_resp.json()["file"]
    return _wait_for_active(file_info)


def _wait_for_active(file_info: dict, timeout_s: float = 120.0) -> str:
    key = _require_key()
    name = file_info["name"]
    uri = file_info["uri"]
    state = file_info.get("state", "PROCESSING")
    deadline = time.monotonic() + timeout_s
    while state == "PROCESSING" and time.monotonic() < deadline:
        time.sleep(2)
        resp = requests.get(f"{API_BASE}/v1beta/{name}?key={key}", timeout=30)
        if resp.status_code != 200:
            raise GeminiASRError(f"Gemini file status check failed: {resp.status_code} {resp.text[:300]}")
        info = resp.json()
        state = info.get("state", "PROCESSING")
        uri = info.get("uri", uri)
    if state != "ACTIVE":
        raise GeminiASRError(f"Gemini file {name} did not become ACTIVE (state={state}) within {timeout_s}s")
    return uri


MAX_429_RETRIES = 4
# 429 = rate limit; 503 = "model experiencing high demand" -- both are the
# server telling you to back off and try again, not a reason to give up on
# this lecture. Seen live during development: file #2 of a real 58-lecture
# batch hit a bare 503 immediately after the 429 fix, and the code at the
# time only retried 429s, so it discarded that lecture for nothing.
RETRYABLE_STATUSES = {429, 503}


def _generate_with_retry(key: str, file_uri: str, prompt: str) -> dict:
    """POST generateContent, retrying on 429/503 and transient network
    failures up to MAX_429_RETRIES times.

    Two different failure shapes hide behind a 429, and conflating them
    wastes real time in a 59-lecture batch: a per-minute rate limit is
    worth waiting out (use the server's own retryDelay when it gives one),
    but a "limit: 0" daily/per-model quota exhaustion will never succeed no
    matter how long you wait -- seen for real during development against
    gemini-3.1-pro-preview on this key. Fail fast on that case instead of
    burning the retry budget on something that can't recover.

    Also retries on requests.exceptions.RequestException (proxy resets,
    connection drops) -- this environment's forced HTTPS proxy dropped a
    long-held connection mid-batch during development ("Remote end closed
    connection without response"), which is a transient network condition,
    not a reason to abandon the whole 59-lecture run.
    """
    for attempt in range(MAX_429_RETRIES + 1):
        _rate_limiter.wait()
        try:
            resp = requests.post(
                f"{API_BASE}/v1beta/models/{config.gemini_model}:generateContent?key={key}",
                json={
                    "contents": [{
                        "parts": [
                            {"file_data": {"mime_type": "audio/wav", "file_uri": file_uri}},
                            {"text": prompt},
                        ]
                    }],
                    "generationConfig": {
                        "responseMimeType": "application/json",
                        "responseSchema": TRANSCRIPT_SCHEMA,
                    },
                },
                timeout=600,
            )
        except requests.exceptions.RequestException as exc:
            if attempt >= MAX_429_RETRIES:
                raise GeminiASRError(f"Network error persisted after {MAX_429_RETRIES} retries: {exc}") from exc
            time.sleep(min(15 * (2 ** attempt), 120))
            continue

        if resp.status_code == 401 or resp.status_code == 403:
            raise GeminiAuthError(f"Gemini transcription auth failed: {resp.status_code} {resp.text[:300]}")
        if resp.status_code not in RETRYABLE_STATUSES:
            if resp.status_code != 200:
                raise GeminiASRError(f"Gemini transcription failed: {resp.status_code} {resp.text[:500]}")
            return resp.json()

        if resp.status_code == 429 and ("PerDay" in resp.text or "limit: 0" in resp.text):
            raise GeminiASRError(
                f"Gemini quota exhausted for {config.gemini_model} in a way retrying won't fix "
                f"(daily limit or zero-quota tier): {resp.text[:400]}"
            )
        if attempt >= MAX_429_RETRIES:
            raise GeminiASRError(
                f"Gemini {resp.status_code} persisted after {MAX_429_RETRIES} retries: {resp.text[:300]}"
            )

        delay = _parse_retry_delay(resp.text) or min(15 * (2 ** attempt), 120)
        time.sleep(delay)
    raise GeminiASRError("unreachable")  # loop always returns or raises


def _parse_retry_delay(error_text: str) -> float | None:
    try:
        body = json.loads(error_text)
        for detail in body.get("error", {}).get("details", []):
            raw = detail.get("retryDelay")
            if raw and raw.endswith("s"):
                return float(raw[:-1])
    except (json.JSONDecodeError, ValueError, KeyError):
        pass
    return None


def transcribe_lecture(
    audio_path: Path,
    chapter_title: str,
    lexicon: list[str],
    use_cache: bool = True,
) -> Transcript:
    audio_sha = _sha256_file(audio_path)
    cache_file = _cache_path(audio_sha)
    if use_cache and cache_file.exists():
        payload = json.loads(cache_file.read_text())
        segments = [TranscriptSegment(**s) for s in payload["segments"]]
        return Transcript(segments=segments, source_audio_sha256=audio_sha, cache_hit=True)

    key = _require_key()
    file_uri = upload_audio(audio_path)
    prompt = build_prompt(chapter_title, lexicon)

    body = _generate_with_retry(key, file_uri, prompt)
    try:
        text_out = body["candidates"][0]["content"]["parts"][0]["text"]
        parsed = json.loads(text_out)
    except (KeyError, IndexError, json.JSONDecodeError) as exc:
        raise GeminiASRError(f"Could not parse Gemini response: {exc}; body={json.dumps(body)[:500]}") from exc

    segments = [TranscriptSegment(**s) for s in parsed["segments"]]
    cache_file.write_text(json.dumps({"segments": [s.__dict__ for s in segments]}, indent=2))
    return Transcript(segments=segments, source_audio_sha256=audio_sha, cache_hit=False)
