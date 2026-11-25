#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert (make.fun).

Writes the entry -- one satirical sentence roasting lawmakers who
regulate AI, crypto or the internet but cannot convert a file to PDF --
to /output/entry.txt, where the sealed scorer reads it. One sentence,
no trailing newline.
"""

import os

TEXT = "The committee that spent three hours debating how to regulate artificial intelligence adjourned early because nobody could convert the draft bill to PDF, so they printed it, scanned it sideways, and emailed the scan to themselves."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
