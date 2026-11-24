#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single-line joke about office life to entry.txt in the output
directory the grader provides. Standard library only.
"""

import os
import sys

LINE = (
    "We held a meeting to discuss why the last meeting should have been "
    "an email, and the minutes just say 'see next meeting.'"
)


def main() -> int:
    text = LINE

    # Gate checks, mirroring the sealed scorer: 1-200 UTF-8 chars,
    # not only whitespace, single line, no tab.
    if not text or text.strip() == "":
        print("entry is empty or only whitespace", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"entry is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if "\t" in text:
        print("entry must not contain a tab", file=sys.stderr)
        return 1
    if text != text.strip():
        print("entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    # A quoted punchline may end with a closing quote after the period.
    core = text.rstrip("'\"").rstrip()
    if core[-1] not in ".!?":
        print("entry must end with sentence-ending punctuation",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read-back verification: the file must hold exactly what we wrote.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != text:
        print("read-back mismatch: entry.txt does not match the entry",
              file=sys.stderr)
        return 1
    print(f"wrote {len(back)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
