"""Structural checks shared by every artifact this project publishes.

Extracted from chem/qa.py once a second family of artifacts (sheets/) needed
the same checks. These are the ones that are true of *any* page published
through the Artifact tool -- no wrapper tags, a complete three-block theme
cascade, tokens defined where they actually apply, the KaTeX scripts present
and in the one order that works, and the size cap.

Subject-specific rules stay with their own caller: chem/qa.py keeps the
exposure-tag polarity and the PYQ-section check, sheets/qa.py keeps the
units-and-figures checks.

Every function here takes comment-stripped HTML. Use strip_html_comments()
first: the templates' own authoring comments name '<html>', '<head>' etc. as
things not to add, and checking raw file text flags those as false positives.
"""
from __future__ import annotations

import re

KATEX_SCRIPTS_IN_ORDER = [
    "katex.min.js",
    "contrib/mhchem.min.js",
    "contrib/auto-render.min.js",
]

Check = tuple[str, bool, str]


def strip_html_comments(html: str) -> str:
    return re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)


def root_token_block(html: str) -> str:
    """The bare `:root { ... }` block -- i.e. NOT inside a @media or
    :root[data-theme=...] selector. A token defined only inside one of those
    never applies in the un-stamped "system" state, which is the classic
    unreadable-artifact bug."""
    m = re.search(r"(?<![\w\-\[\]\"'=(:.])\:root\s*\{([^}]*)\}", html)
    return m.group(1) if m else ""


def structural_checks(html: str, stripped: str, *, math_root_id: str | None = None) -> list[Check]:
    """html: the raw file (for the byte-size check).
    stripped: the same file with HTML comments removed.
    math_root_id: if given, also assert renderMathInElement targets this id."""
    checks: list[Check] = []

    def check(name: str, passed: bool, detail: str = "") -> None:
        checks.append((name, passed, detail))

    check(
        "no doctype/html/head/body wrapper",
        not re.search(r"<!doctype|<html[ >]|<head[ >]|<body[ >]", stripped, re.IGNORECASE),
    )

    top_level_open = re.findall(r"<details\b[^>]*\bopen\b", stripped, re.IGNORECASE)
    check("no top-level <details open>", len(top_level_open) == 0, f"{len(top_level_open)} found")

    root_block = root_token_block(stripped)
    defined = set(re.findall(r"--([\w-]+)\s*:", root_block))
    used = set(re.findall(r"var\(--([\w-]+)\)", stripped))
    undefined = sorted(t for t in used if t not in defined)
    check(
        "every var(--token) defined in bare :root",
        not undefined,
        f"undefined: {undefined}" if undefined else "",
    )

    has_media_dark = bool(
        re.search(
            r'prefers-color-scheme:\s*dark\s*\)\s*\{[^}]*:root:not\(\[data-theme="light"\]\)',
            stripped,
            re.DOTALL,
        )
    )
    check("prefers-color-scheme dark block present", has_media_dark)
    check(
        "[data-theme=dark] override block present",
        bool(re.search(r':root\[data-theme="dark"\]\s*\{', stripped)),
    )
    check(
        "body sets background from a token",
        bool(re.search(r"\bbody\s*\{[^}]*background\s*:\s*var\(--", stripped, re.DOTALL)),
    )

    positions = []
    for script in KATEX_SCRIPTS_IN_ORDER:
        m = re.search(re.escape(script), stripped)
        positions.append(m.start() if m else None)
    all_present = all(p is not None for p in positions)
    check("KaTeX + mhchem + auto-render scripts present", all_present, str(positions))
    check("KaTeX scripts in required order", all_present and positions == sorted(positions))

    call = re.search(r'getElementById\(["\'](.+?)["\']\)', stripped)
    if call:
        target = call.group(1)
        exists = bool(re.search(rf'id=["\']{re.escape(target)}["\']', stripped))
        if math_root_id is not None and target != math_root_id:
            check("renderMathInElement target id exists in document", False,
                  f"targets {target!r}, expected {math_root_id!r}")
        else:
            check("renderMathInElement target id exists in document", exists, target)
    else:
        check("renderMathInElement target id exists in document", False, "no getElementById call found")

    size_mb = len(html.encode("utf-8")) / (1024 * 1024)
    check("file under 16 MB", size_mb < 16, f"{size_mb:.2f} MB")

    return checks


def title_check(stripped: str, expected_title: str) -> Check:
    m = re.search(r"<title>(.*?)</title>", stripped, re.DOTALL)
    actual = m.group(1).strip() if m else None
    return (
        "title matches maps.json exactly",
        actual == expected_title,
        f"got {actual!r}, want {expected_title!r}",
    )


def report(checks: list[Check]) -> bool:
    """Print each check and return True iff all passed."""
    ok = True
    for name, passed, detail in checks:
        flag = "PASS" if passed else "FAIL"
        suffix = f" — {detail}" if detail else ""
        print(f"[{flag}] {name}{suffix}")
        ok = ok and passed
    print()
    print(f"{sum(1 for _, p, _ in checks if p)}/{len(checks)} checks passed.")
    return ok
