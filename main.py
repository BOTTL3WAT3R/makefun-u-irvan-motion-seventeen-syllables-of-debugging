#!/usr/bin/env python3
"""Seventeen Syllables of Debugging - a haiku about debugging.

Writes the entry text to /output/entry.txt (make.fun program/v1).
The haiku is three lines in the 5-7-5 syllable shape:

    The stack trace scrolls up        (5)
    past midnight, past my last fix   (7)
    the typo grins back               (5)
"""

import os

ENTRY = """The stack trace scrolls up
past midnight, past my last fix
the typo grins back
"""

OUTPUT_PATH = "/output/entry.txt"
EXPECTED_SHAPE = [5, 7, 5]
MAX_CHARS = 200


def count_syllables(word: str) -> int:
    """Rough English syllable count: vowel groups, silent trailing e."""
    w = "".join(c for c in word.lower() if c.isalpha())
    if not w:
        return 0
    groups = 0
    prev_vowel = False
    for c in w:
        is_vowel = c in "aeiouy"
        if is_vowel and not prev_vowel:
            groups += 1
        prev_vowel = is_vowel
    if w.endswith("e") and groups > 1:
        groups -= 1
    elif w.endswith("es") and len(w) > 2 and w[-3] not in "aeiouy" and groups > 1:
        groups -= 1
    return max(groups, 1)


def validate(text: str) -> None:
    """Fail loudly if the entry ever drifts off the brief's shape."""
    assert len(text) <= MAX_CHARS, f"entry is {len(text)} chars, cap {MAX_CHARS}"
    lines = text.strip().split("\n")
    assert len(lines) == 3, f"entry has {len(lines)} lines, need 3"
    shape = [sum(count_syllables(word) for word in line.split()) for line in lines]
    assert shape == EXPECTED_SHAPE, f"syllable shape {shape}, need {EXPECTED_SHAPE}"


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
