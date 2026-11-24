#!/usr/bin/env python3
"""Write one office-life joke to /output/entry.txt (or $OUTPUT_DIR/entry.txt)."""

import os

JOKE = "My calendar finally had a free hour, so I spent it in a meeting about why nobody has free time."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
