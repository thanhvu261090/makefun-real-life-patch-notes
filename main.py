#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

Writes one funny one-line patch note for a bug in real life or human
biology to /output/entry.txt, after checking it against the kit's gate:
UTF-8 text, 1 to 160 characters, not only whitespace.
"""

import os
import sys

ENTRY = (
    "v4.0.2: fixed a bug where yawning in a meeting replicated itself "
    "to every attendee without consent."
)

MAX_CHARS = 160


def gate_check(text: str) -> None:
    """Enforce the kit gate: 1-160 UTF-8 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    text.encode("utf-8")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing padding")


def main() -> int:
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
