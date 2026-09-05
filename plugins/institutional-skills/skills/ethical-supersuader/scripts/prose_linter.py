#!/usr/bin/env python3
"""Lightweight prose linter for the Beautiful Prose / Ethical Supersuader skill.

This is a quality tool, not an AI detector. It flags patterns that usually weaken
prose: filler transitions, cheap pivots, over-smooth cadence, hidden verbs, and
generic intensifiers. It never rewrites text by itself.
"""

from __future__ import annotations

import argparse
import re
import statistics
import sys
from pathlib import Path


BANNED_PHRASES = [
    "at its core",
    "in today's world",
    "in today's landscape",
    "in a world where",
    "it is important to note",
    "what this means is",
    "that said",
    "ultimately",
    "furthermore",
    "moreover",
    "let's explore",
    "delve",
    "unlock",
    "seamless",
    "game-changing",
    "transformative",
    "the real story is",
    "here are the key takeaways",
    "in conclusion",
    "wanted to reach out",
    "circling back",
    "circle back",
    "touch base",
    "checking in",
    "looping in",
    "move forward",
    "moving forward",
    "at scale",
    "drive value",
    "unlock value",
    "best-in-class",
    "mission-critical",
    "north star",
    "double-click",
    "net-net",
    "low-hanging fruit",
    "deep dive",
]

THERAPY_PHRASES = [
    "i hear you",
    "that sounds hard",
    "you're valid",
    "give yourself grace",
    "be kind to yourself",
]

GENERIC_INTENSIFIERS = [
    "robust",
    "critical",
    "vital",
    "meaningful",
    "dynamic",
    "nuanced",
    "compelling",
    "powerful",
    "innovative",
    "important",
]

CORPORATE_OPERATOR_JARGON = [
    "lane",
    "lanes",
    "cleaner",
    "cleanly",
    "cleanest",
    "seam",
    "leverage",
    "surface",
    "align",
    "alignment",
    "streamline",
    "stakeholder",
    "ecosystem",
]

NOMINALIZATION_SUFFIXES = (
    "tion",
    "sion",
    "ment",
    "ance",
    "ence",
    "ity",
)


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def line_col(text: str, index: int) -> tuple[int, int]:
    before = text[:index]
    line = before.count("\n") + 1
    col = index - before.rfind("\n")
    return line, col


def find_phrase_hits(text: str, phrases: list[str], label: str) -> list[str]:
    hits: list[str] = []
    for phrase in phrases:
        escaped = re.escape(phrase).replace(r"\ ", r"\s+")
        pattern = rf"(?<!\w){escaped}(?!\w)"
        for match in re.finditer(pattern, text, re.IGNORECASE):
            line, col = line_col(text, match.start())
            hits.append(f"{label}: line {line}, col {col}: {phrase}")
    return hits


def cheap_pivot_hits(text: str) -> list[str]:
    patterns = [
        r"\bnot\s+only\b.+?\bbut\s+also\b",
        r"\bnot\s+[^.?!]{1,80},?\s+but\s+[^.?!]{1,80}",
        r"\bthis\s+is(?:n't| not)\s+about\b.+?\bit(?:'s| is)\s+about\b",
    ]
    hits: list[str] = []
    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE | re.DOTALL):
            line, col = line_col(text, match.start())
            sample = " ".join(match.group(0).split())[:140]
            hits.append(f"cheap pivot: line {line}, col {col}: {sample}")
    return hits


def throat_clearing_hits(text: str) -> list[str]:
    """Flag announcements of writing that delay the actual message."""
    pattern = r"\bI\s+(?:(?:just\s+)?wanted\s+to\s+(?:put\s+(?:this|it)\s+in\s+writing|write|reach\s+out)|(?:am|'m)\s+writing\s+to)\b"
    hits = []
    for match in re.finditer(pattern, text, re.IGNORECASE):
        line, col = line_col(text, match.start())
        hits.append(f"throat clearing: line {line}, col {col}: {match.group(0)}")
    return hits


def em_dash_hits(text: str) -> list[str]:
    hits: list[str] = []
    for match in re.finditer(r"—|--", text):
        line, col = line_col(text, match.start())
        hits.append(f"em dash / double hyphen: line {line}, col {col}")
    return hits


def sentence_rhythm_hits(text: str) -> list[str]:
    sentences = split_sentences(text)
    if len(sentences) < 5:
        return []
    lengths = [len(re.findall(r"\b[\w']+\b", s)) for s in sentences]
    hits: list[str] = []

    for i in range(len(lengths) - 4):
        window = lengths[i : i + 5]
        if max(window) - min(window) <= 4:
            hits.append(
                "flat rhythm: sentences "
                f"{i + 1}-{i + 5} have similar lengths {window}"
            )

    if len(lengths) >= 8 and statistics.pstdev(lengths) < 5:
        hits.append(
            "flat rhythm: low sentence-length variance across the whole piece "
            f"{lengths}"
        )
    return hits


def repeated_opening_hits(text: str) -> list[str]:
    sentences = split_sentences(text)
    openings: dict[str, list[int]] = {}
    for i, sentence in enumerate(sentences, start=1):
        words = re.findall(r"\b[\w']+\b", sentence.lower())
        if not words:
            continue
        opener = " ".join(words[:2]) if len(words) > 1 else words[0]
        openings.setdefault(opener, []).append(i)
    return [
        f"repeated opening: '{opener}' starts sentences {positions}"
        for opener, positions in sorted(openings.items())
        if len(positions) >= 3
    ]


def nominalization_hits(text: str) -> list[str]:
    hits: list[str] = []
    words = list(re.finditer(r"\b[a-zA-Z]{8,}\b", text))
    for match in words:
        word = match.group(0)
        lower = word.lower()
        if lower.endswith(NOMINALIZATION_SUFFIXES):
            line, col = line_col(text, match.start())
            hits.append(f"possible hidden verb: line {line}, col {col}: {word}")
    return hits[:50]


def lint(text: str) -> list[str]:
    hits: list[str] = []
    hits.extend(em_dash_hits(text))
    hits.extend(find_phrase_hits(text, BANNED_PHRASES, "banned/filler phrase"))
    hits.extend(find_phrase_hits(text, THERAPY_PHRASES, "therapy voice"))
    hits.extend(find_phrase_hits(text, GENERIC_INTENSIFIERS, "generic intensifier"))
    hits.extend(find_phrase_hits(text, CORPORATE_OPERATOR_JARGON, "corporate/operator jargon"))
    hits.extend(cheap_pivot_hits(text))
    hits.extend(throat_clearing_hits(text))
    hits.extend(sentence_rhythm_hits(text))
    hits.extend(repeated_opening_hits(text))
    hits.extend(nominalization_hits(text))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Flag common prose slop patterns.")
    parser.add_argument("path", nargs="?", help="Text/markdown file to lint. Reads stdin if omitted.")
    args = parser.parse_args()

    if args.path:
        text = Path(args.path).read_text(errors="ignore")
    else:
        text = sys.stdin.read()

    hits = lint(text)
    if not hits:
        print("prose_lint: pass")
        return 0

    print(f"prose_lint: {len(hits)} issue(s)")
    for hit in hits:
        print(f"- {hit}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
