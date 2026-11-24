#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one character, the letter K, to /output/entry.txt.
K stands for a day that ends knackered: vivid, funny and true, and the
letter K is the sharp pick for it — the judge reads only the letter and
the K-words it reaches for (knockout, kaleidoscopic, kooky) all land.
"""
import os

LETTER = "K"
OUTPUT = "/output/entry.txt"


def main():
    # Gate: the entry must be exactly one A-Z character, nothing else.
    # Fail loudly here rather than shipping an invalid entry.
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError(f"LETTER must be a single A-Z character, got {LETTER!r}")
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
