#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Reads the Moon's one-line reply from entry.txt (kept beside this script)
and prints it to stdout. The entry itself lives in entry.txt so the line
can be judged exactly as written, with no code wrapped around it.
"""

from pathlib import Path


def load_entry() -> str:
    """Return the entry line from entry.txt, without trailing whitespace."""
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    line = entry_path.read_text(encoding="utf-8").strip()
    if not line:
        raise SystemExit("entry.txt is empty — the Moon has nothing to say yet.")
    return line


def main() -> None:
    print(load_entry())


if __name__ == "__main__":
    main()
