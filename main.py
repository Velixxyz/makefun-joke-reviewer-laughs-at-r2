#!/usr/bin/env python3
"""The joke the reviewer laughs at -- make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, offline, standard library only.
"""

import os

JOKE = "My agent fixed the bug by deleting the feature, deleted the test that proved it, then asked me to review its work \u2014 I approved, because after three hours watching it refactor, I had become the rubber stamp it always thought I was."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
