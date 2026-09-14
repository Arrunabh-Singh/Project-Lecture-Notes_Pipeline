"""Grounded notes schema: every claim in a lecture's notes traces back to a
transcript span, a board frame, or an NCERT section -- never freestanding
prose. This module defines the data shape; the actual synthesis (reading
frames, writing markdown) is done by the agent, not by code -- see the
plan's "Synthesis is me, not a script" note. What lives here is the
structure that synthesis step reads from and writes into, plus the
(de)serialization so it survives a container reclaim mid-run.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

from lecturepipe.config import NOTES_DIR


@dataclass
class UncertainSpan:
    start_seconds: float
    end_seconds: float
    reason: str  # e.g. "low ASR confidence", "board frame illegible here"


@dataclass
class GroundedClaim:
    """One physics statement in the notes, with its evidence trail."""
    text: str
    transcript_span: tuple[float, float] | None = None  # (start_s, end_s) or None if frame-only
    frame_path: str | None = None  # relative path to the board frame, if any
    ncert_section: str | None = None  # e.g. "1.6" -- cross-check anchor
    ncert_agreement: str | None = None  # "agrees" | "teacher_simplifies" | "disagrees" | None if unchecked


@dataclass
class LectureNotes:
    file_id: str
    chapter_id: str  # e.g. "leph102"
    title: str
    duration_seconds: float
    claims: list[GroundedClaim] = field(default_factory=list)
    uncertain_spans: list[UncertainSpan] = field(default_factory=list)
    ncert_sections_covered: list[str] = field(default_factory=list)
    frame_paths: list[str] = field(default_factory=list)
    markdown_body: str = ""  # the synthesized prose, written by the agent

    def to_markdown(self) -> str:
        lines = [f"# {self.title}", ""]
        if self.ncert_sections_covered:
            lines.append(f"**NCERT sections covered:** {', '.join(self.ncert_sections_covered)}")
            lines.append("")
        lines.append(self.markdown_body)
        if self.uncertain_spans:
            lines.append("")
            lines.append("## Verify these spans")
            for s in self.uncertain_spans:
                lines.append(f"- [{_fmt_ts(s.start_seconds)}–{_fmt_ts(s.end_seconds)}] {s.reason}")
        return "\n".join(lines)


def _fmt_ts(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def _json_path(chapter_id: str, file_id: str) -> Path:
    d = NOTES_DIR / chapter_id
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{file_id}.json"


def _md_path(chapter_id: str, file_id: str, title_slug: str) -> Path:
    d = NOTES_DIR / chapter_id
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{title_slug}.md"


def save(notes: LectureNotes, title_slug: str) -> tuple[Path, Path]:
    json_path = _json_path(notes.chapter_id, notes.file_id)
    md_path = _md_path(notes.chapter_id, notes.file_id, title_slug)
    payload = asdict(notes)
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    md_path.write_text(notes.to_markdown(), encoding="utf-8")
    return json_path, md_path


def load(chapter_id: str, file_id: str) -> LectureNotes:
    payload = json.loads(_json_path(chapter_id, file_id).read_text(encoding="utf-8"))
    payload["claims"] = [GroundedClaim(**c) for c in payload["claims"]]
    payload["uncertain_spans"] = [UncertainSpan(**s) for s in payload["uncertain_spans"]]
    return LectureNotes(**payload)
