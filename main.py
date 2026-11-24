#!/usr/bin/env python3
"""Seventeen Syllables of Debugging - a haiku entry for make.fun.

The poem is stored as data. At run time every word is looked up in a
syllable table, each line is totalled, and the entry is written only
if the 5-7-5 shape holds and the text fits the 1-200 character gate.
"""
from pathlib import Path

LINES = [
    "Blame points at my name",
    "three winters back, I wrote it",
    "past me sends regards",
]

SYLLABLES = {
    "blame": 1,
    "points": 1,
    "at": 1,
    "my": 1,
    "name": 1,
    "three": 1,
    "winters": 2,
    "back": 1,
    "i": 1,
    "wrote": 1,
    "it": 1,
    "past": 1,
    "me": 1,
    "sends": 1,
    "regards": 2,
}

SHAPE = (5, 7, 5)
MIN_CHARS = 1
MAX_CHARS = 200


def count_line(line):
    total = 0
    for raw in line.split():
        word = raw.strip(",.!?;:").lower()
        if word not in SYLLABLES:
            raise SystemExit(f"no syllable count recorded for {word!r}")
        total += SYLLABLES[word]
    return total


def render():
    if len(LINES) != 3:
        raise SystemExit(f"a haiku has three lines, found {len(LINES)}")
    counts = tuple(count_line(line) for line in LINES)
    if counts != SHAPE:
        raise SystemExit(f"haiku shape broken: {counts} != {SHAPE}")
    text = "\n".join(LINES)
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry length out of range: {len(text)}")
    return text + "\n"


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
