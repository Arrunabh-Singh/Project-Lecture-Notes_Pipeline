"""Parse raw NCERT chapter text (extracted via the Drive connector's
read_file_content, which flattens PDF text and loses layout/bold/italic
markup) into a structured outline: section tree, named scientists,
a grounded technical lexicon, and the Summary / Points to Ponder /
Exercises blocks.

This is heuristic, not a real PDF-structure parser -- the connector gives
us plain text with page-break artifacts ("Reprint 2026-27") and duplicated
drop-cap runs (e.g. "2.1 I2.1 I2.1 INTRODUCTION NTRODUCTION..."). Every
extracted term is a literal substring of the source text: nothing here is
invented, so it is safe to use as an ASR lexicon and a cross-check
reference, but it should not be trusted as a faithful section-by-section
transcription of the book -- that's what the "fidelity" field records.

CHAPTER_META provenance:
  full_raw_extract  -- raw connector dump, unedited, parsed by regex here.
  condensed_summary -- hand-condensed from a full connector read that
                        exceeded this session's inline context budget;
                        structure/equations preserved, prose trimmed.
Both are grounded in the actual NCERT text. Neither should be used as a
source for exact equation transcription in the notes pipeline -- board
frames are the authority for equations (see plan: "NCERT equation
extraction is unreliable").
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

RAW_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "ncert" / "raw"
OUT_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "ncert" / "processed"

CHAPTER_META = {
    "leph101": {"num": 1, "title": "Electric Charges and Fields", "fidelity": "full_raw_extract"},
    "leph102": {"num": 2, "title": "Electrostatic Potential and Capacitance", "fidelity": "full_raw_extract"},
    "leph103": {"num": 3, "title": "Current Electricity", "fidelity": "full_raw_extract"},
    "leph104": {"num": 4, "title": "Moving Charges and Magnetism", "fidelity": "full_raw_extract"},
    "leph105": {"num": 5, "title": "Magnetism and Matter", "fidelity": "condensed_summary"},
    "leph106": {"num": 6, "title": "Electromagnetic Induction", "fidelity": "condensed_summary"},
    "leph107": {"num": 7, "title": "Alternating Current", "fidelity": "condensed_summary"},
    "leph108": {"num": 8, "title": "Electromagnetic Waves", "fidelity": "condensed_summary"},
}

# Maps chapter id -> lecture folder name, established during Drive discovery.
CHAPTER_TO_LECTURE_FOLDER = {
    "leph101": "Ch1 Electric field",
    "leph102": "Ch2 Electric potential",
    "leph103": "Ch3 electricity",
    "leph104": "Ch4 moving charges and magnetism",
    "leph105": "Ch5 matter and magnetism",
    "leph106": "Ch6 EMI",
    "leph107": "Ch7AC",
    "leph108": "Ch8 EM Waves",
}

SECTION_RE = re.compile(
    r"(?:^|\n|(?<=\s))(?P<num>\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)\s+"
    r"(?P<head>[A-Z][A-Z0-9 ,&:\-‐-―'‘’]{3,70}?)"
    r"(?=\n|\s+[A-Z][a-z])"
)

SCIENTIST_RE = re.compile(
    r"(?P<name>[A-Z][A-Za-z.’' \-]{2,40}?)\s*"
    r"[\(\[]\s*(?P<birth>\d{3,4})\s*[–—\-]\s*(?P<death>\d{3,4})\s*[\)\]]"
)

STOPWORDS = {
    "THE", "AND", "FOR", "WITH", "FROM", "THIS", "THAT", "WHICH", "WHERE",
    "WHEN", "THEN", "THAN", "THESE", "THOSE", "INTO", "OVER", "ALSO",
    "SUCH", "EACH", "SOME", "MORE", "MOST", "ONLY", "VERY", "WILL",
}

# Whole-phrase noise from worked-example boilerplate ("Solution Let q1..."),
# not physics vocabulary -- drop rather than lexicon-poison the ASR prompt.
NOISE_PHRASES = {
    "solution", "example", "figure", "chapter", "note", "consider",
    "let", "here", "since", "using", "given", "find", "obtain", "show",
}


def _is_noise_phrase(phrase: str) -> bool:
    return any(w.lower() in NOISE_PHRASES for w in phrase.split())


def _dedupe_dropcap_runs(text: str) -> str:
    """Collapse PDF drop-cap artifacts like
    'I2.1 I2.1 I2.1 INTRODUCTION NTRODUCTION NTRODUCTION' -> 'INTRODUCTION'.
    Heuristic: a short token immediately repeated 3+ times in a row."""
    return re.sub(r"\b(\w{1,15})(?:\s+\1){2,}\b", r"\1", text)


def _find_boundary(text: str, marker: str, start: int = 0) -> int | None:
    idx = text.find(marker, start)
    return idx if idx != -1 else None


def _extract_sections(text: str) -> list[dict]:
    sections = []
    seen = set()
    for m in SECTION_RE.finditer(text):
        num, head = m.group("num"), m.group("head").strip()
        head = re.sub(r"\s+", " ", head)
        # Filter worked-example numbering ("Example 1.1") which reuses N.N
        # but is followed by lowercase prose, not an all-caps heading.
        letters = re.sub(r"[^A-Za-z]", "", head)
        if not letters or not letters.isupper() or len(letters) < 4:
            continue
        if head in STOPWORDS:
            continue
        key = (num, head)
        if key in seen:
            continue
        seen.add(key)
        # str.title() capitalizes the letter after an apostrophe too
        # ("Coulomb'S Law") since it treats it as a word boundary; fix that
        # one case up rather than hand-rolling a full title-case function.
        titled = re.sub(r"(['‘’])([A-Z])", lambda m: m.group(1) + m.group(2).lower(), head.title())
        sections.append({"number": num, "heading": titled})
    return sections


def _extract_scientists(text: str) -> list[dict]:
    out = []
    seen = set()
    for m in SCIENTIST_RE.finditer(text):
        name = re.sub(r"\s+", " ", m.group("name")).strip(" .")
        if name in seen or len(name.split()) > 5:
            continue
        seen.add(name)
        out.append({"name": name, "years": f"{m.group('birth')}–{m.group('death')}"})
    return out


def _extract_block(text: str, start_marker: str, end_markers: list[str]) -> str | None:
    start = _find_boundary(text, start_marker)
    if start is None:
        return None
    start += len(start_marker)
    end = len(text)
    for marker in end_markers:
        idx = _find_boundary(text, marker, start)
        if idx is not None:
            end = min(end, idx)
    return text[start:end].strip()


def _build_lexicon(text: str, sections: list[dict], scientists: list[dict]) -> list[str]:
    terms: set[str] = set()
    for s in sections:
        for word in s["heading"].split():
            w = word.strip(",.'&")
            if len(w) > 3 and w.upper() not in STOPWORDS:
                terms.add(w)
        if len(s["heading"].split()) <= 5:
            terms.add(s["heading"])
    for sci in scientists:
        terms.add(sci["name"])
    # Frequency-based technical bigrams: consecutive Capitalized words
    # repeated 2+ times in the body (e.g. "Electric Field", "Gauss Law").
    bigrams = re.findall(r"\b([A-Z][a-z]{2,}\s+[A-Z][a-z]{2,})\b", text)
    from collections import Counter
    counts = Counter(bigrams)
    for phrase, n in counts.items():
        if n < 2 or _is_noise_phrase(phrase):
            continue
        if any(w.upper() in STOPWORDS for w in phrase.split()):
            continue
        terms.add(phrase)
    return sorted(terms)


def parse_chapter(chapter_id: str) -> dict:
    meta = CHAPTER_META[chapter_id]
    raw_path = RAW_DIR / f"{chapter_id}.txt"
    text = _dedupe_dropcap_runs(raw_path.read_text(encoding="utf-8"))

    sections = _extract_sections(text)
    scientists = _extract_scientists(text)
    lexicon = _build_lexicon(text, sections, scientists)

    summary = _extract_block(text, "SUMMARY", ["POINTS TO PONDER", "EXERCISES"])
    ponder = _extract_block(text, "POINTS TO PONDER", ["EXERCISES"])
    exercises = _extract_block(text, "EXERCISES", ["Reprint 2026-27\n\n\n", "\x00"])
    if exercises:
        # Trim to first ~6000 chars in case the boundary regex over-ran.
        exercises = exercises[:8000]

    return {
        "chapter_id": chapter_id,
        "chapter_number": meta["num"],
        "title": meta["title"],
        "fidelity": meta["fidelity"],
        "lecture_folder": CHAPTER_TO_LECTURE_FOLDER[chapter_id],
        "source_note": "NCERT Class 12 Physics Part I, Reprint 2026-27 "
                       "(RATIONALISED 2022-23) -- current CBSE syllabus. "
                       "Equations NOT reliable in this extraction; use board "
                       "frames as the equation source of truth.",
        "sections": sections,
        "scientists": scientists,
        "lexicon": lexicon,
        "summary": summary,
        "points_to_ponder": ponder,
        "exercises": exercises,
        "raw_char_count": len(text),
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    index = []
    for chapter_id in CHAPTER_META:
        raw_path = RAW_DIR / f"{chapter_id}.txt"
        if not raw_path.exists():
            print(f"SKIP {chapter_id}: no raw file at {raw_path}")
            continue
        outline = parse_chapter(chapter_id)
        out_path = OUT_DIR / f"{chapter_id}.json"
        out_path.write_text(json.dumps(outline, indent=2, ensure_ascii=False), encoding="utf-8")
        print(
            f"{chapter_id}: {len(outline['sections'])} sections, "
            f"{len(outline['scientists'])} scientists, "
            f"{len(outline['lexicon'])} lexicon terms "
            f"[{outline['fidelity']}] -> {out_path}"
        )
        index.append({
            "chapter_id": chapter_id,
            "chapter_number": outline["chapter_number"],
            "title": outline["title"],
            "lecture_folder": outline["lecture_folder"],
            "fidelity": outline["fidelity"],
            "section_count": len(outline["sections"]),
            "lexicon_size": len(outline["lexicon"]),
        })
    (OUT_DIR / "_index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(f"\nWrote index of {len(index)} chapters -> {OUT_DIR / '_index.json'}")


if __name__ == "__main__":
    main()
