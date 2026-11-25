#!/usr/bin/env python3
"""Write one short family scene to $MAKEFUN_OUTPUT_DIR/entry.txt.

The scene is a single warm, funny, heartfelt domestic moment, written
for make.fun's "Make the AI Judge Feel Proud: A Family Scene" bounty.
The gate requires UTF-8 text of 1 to 280 characters, in one or two
lines, so this program validates the text before and after writing it.
"""

import os
import sys

ENTRY = (
    "Dad still sets a place for Mom at Sunday dinner, three years after "
    "she passed \u2014 then winks at me and says, 'She'd kill me if I let "
    "the good plates gather dust.' We eat, we laugh, and somehow she's "
    "still at the table."
)

MAX_CHARS = 280
MAX_LINES = 2


def main() -> int:
    text = ENTRY
    if not text.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} characters, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    lines = text.splitlines()
    if len(lines) > MAX_LINES:
        print(
            f"error: entry has {len(lines)} lines, over the "
            f"{MAX_LINES} limit",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; fall back to a plain path if a
    # full file path was given instead.
    if out_dir.endswith(".txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("error: re-read entry does not match byte for byte",
              file=sys.stderr)
        return 1

    print(f"Wrote {len(text)} characters to {path}:")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
