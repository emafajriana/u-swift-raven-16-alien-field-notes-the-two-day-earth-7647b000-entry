#!/usr/bin/env python3
"""Entry for make.fun: 'Alien Field Notes: The Two Day Earth Review'.

Writes one line — an alien tourist's review of planet Earth — to the
output entry file. Stdlib only, deterministic.
"""

import os
import sys

LINE = (
    "Day two: before eating, humans photograph the meal and send it to "
    "absent friends, whose tiny hearts grant permission to begin. "
    "Four stars; the food went cold waiting for approval."
)

MAX_CHARS = 200


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify(path: str) -> None:
    """Read the written file back and check it against the gate:
    UTF-8 text of 1 to 200 characters, not only white space, exactly
    one line, and byte-for-byte the intended entry."""
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    if text != LINE:
        raise SystemExit("gate: written text does not match the entry")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"gate: {len(text)} chars, outside 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("gate: entry is only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate: entry must be a single line")


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    verify(path)
    print(f"wrote {len(LINE)} chars to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
