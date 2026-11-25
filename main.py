#!/usr/bin/env python3
"""make.fun entry: The Internet in One Word.

Writes a single word describing the whole internet to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints it.
"""

import os

WORD = "Brainrot"  # 8 chars; gate requires 1-30 chars of non-whitespace UTF-8


def main() -> None:
    word = WORD.strip()
    assert 1 <= len(word) <= 30 and word.strip(), "entry fails the 1-30 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word + "\n")
    print(word)


if __name__ == "__main__":
    main()
