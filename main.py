#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters: one Wi-Fi network name.

The name is "TheWiFiOutlivedOurMarriage" -- twenty-six characters.

The marriage is over and the Wi-Fi is still broadcasting. That is the
whole settlement in six words: two people, one failed marriage, and a
router that outlasted them both.

Stdlib only. No network, no randomness, no clock: the same name every run.
"""

import os
import sys

NAME = "TheWiFiOutlivedOurMarriage"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(NAME)
    print(NAME)
    return 0


if __name__ == "__main__":
    sys.exit(main())
