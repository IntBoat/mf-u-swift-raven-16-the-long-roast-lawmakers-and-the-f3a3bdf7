#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "They can draft a bill to regulate the internet by Tuesday, yet the committee's own report is still a scanned photo of a printout, and nobody in the building knows how to turn it into a PDF."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
