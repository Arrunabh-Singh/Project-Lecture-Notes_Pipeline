"""Coverage-gap analysis: which NCERT sections a chapter's lectures never
touch. This is computed, not synthesized -- a lecture's ncert_sections_covered
list (populated by the agent during notes synthesis, based on what was
actually taught) is diffed against the chapter's full section tree from
ncert/outline.py's output."""
from __future__ import annotations

import json
from dataclasses import dataclass

from lecturepipe.config import NCERT_DIR
from lecturepipe.notes import LectureNotes


@dataclass
class CoverageGap:
    chapter_id: str
    section_number: str
    heading: str


def chapter_sections(chapter_id: str) -> list[dict]:
    path = NCERT_DIR / f"{chapter_id}.json"
    if not path.exists():
        return []
    outline = json.loads(path.read_text(encoding="utf-8"))
    return outline["sections"]


def find_gaps(chapter_id: str, lectures: list[LectureNotes]) -> list[CoverageGap]:
    covered: set[str] = set()
    for lecture in lectures:
        covered.update(lecture.ncert_sections_covered)

    gaps = []
    for section in chapter_sections(chapter_id):
        if section["number"] not in covered:
            gaps.append(CoverageGap(
                chapter_id=chapter_id,
                section_number=section["number"],
                heading=section["heading"],
            ))
    return gaps


def coverage_summary(chapter_id: str, lectures: list[LectureNotes]) -> dict:
    total = chapter_sections(chapter_id)
    gaps = find_gaps(chapter_id, lectures)
    covered_count = len(total) - len(gaps)
    return {
        "chapter_id": chapter_id,
        "total_sections": len(total),
        "covered_sections": covered_count,
        "gap_count": len(gaps),
        "gaps": [{"number": g.section_number, "heading": g.heading} for g in gaps],
    }
