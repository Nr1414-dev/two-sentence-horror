#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes one horror story of exactly two sentences (224 characters) to
/output/entry.txt, per the bounty gate (UTF-8 text, 1-400 characters).
"""

import os

ENTRY = (
    "The priest said my confession from last week was beautiful, "
    "and asked me to come again. "
    "I haven't been to church in ten years, and the confession he described "
    "was mine \u2014 word for word, including the part I never told anyone."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Brief-format guard: exactly two sentences, 1-400 chars, no
    period-abbreviations (e.g. 'a.m.') that a naive sentence counter
    would misread as extra sentences."""
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry length {len(text)} outside 1-400 chars")
    if ".a.m." in text or ".p.m." in text:
        raise ValueError("entry must not contain a.m./p.m. abbreviations")
    if text.count(". ") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly two sentences")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back verification: the written file must match the entry exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: file content != ENTRY")


if __name__ == "__main__":
    main()
