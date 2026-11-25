#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters: one Wi-Fi network name.

The name is "TheWiFiOutlivedOurMarriage" -- twenty-six characters.

The marriage is over and the Wi-Fi is still broadcasting. That is the
whole settlement in six words: two people, one failed marriage, and a
router that outlasted them both. The joke lands because the router is the
only thing in the house that kept its promise; the story is the divorce
the name never has to describe.

Stdlib only. No network, no randomness, no clock: the same name every run.
"""

import os
import sys

NAME = "TheWiFiOutlivedOurMarriage"

# The bounty gate: UTF-8 text of 1 to 32 characters, not only whitespace.
MAX_CHARS = 32


def gate(name):
    """Refuse anything the sealed scorer would refuse."""
    if not name or not name.strip():
        raise ValueError("name must not be empty or only whitespace")
    if name.strip() != name:
        raise ValueError("name must not start or end with whitespace")
    if len(name) > MAX_CHARS:
        raise ValueError("name must be at most %d characters" % MAX_CHARS)
    if any(ord(c) < 32 or ord(c) == 127 for c in name):
        raise ValueError("name must not contain control characters")
    if not name.isascii():
        raise ValueError("name must be plain ASCII")
    return name


def main():
    name = gate(NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(name)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != name:
            raise RuntimeError("entry.txt does not hold the name we wrote")
    print(name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
