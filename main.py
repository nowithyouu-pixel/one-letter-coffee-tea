#!/usr/bin/env python3
"""Entry for make.fun's "One Letter: Coffee or Tea" bounty.

Writes exactly one letter, A (coffee), to /output/entry.txt.
No network, no input, deterministic.
"""

import os

LETTER = "A"  # A = coffee: the drink you have before you are a person.
DRINK = "coffee"


def main() -> None:
    if len(LETTER) != 1 or LETTER not in ("A", "B"):
        raise ValueError(f"entry must be exactly one letter, A or B, got {LETTER!r}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
