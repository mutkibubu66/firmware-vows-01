#!/usr/bin/env python3
"""Write one original robot wedding vow to /output/entry.txt.

Pure standard library, no network. The vow is a single line: a robot
promising its partner love through every update, crash and low-battery
warning, closing on the wedding classic "till firmware do us part".
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_vow() -> str:
    """Return the entry line: vow setup, then the payoff at the end."""
    return (
        "I promise to love you through every update, every crash, "
        "and every 2% battery warning \u2014 till firmware do us part."
    )


VOW = get_vow()


def validate(line: str) -> None:
    """Enforce the gate: 1-200 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(VOW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(VOW + "\n")
    print(VOW)


if __name__ == "__main__":
    main()
