#!/usr/bin/env python3
"""Write one sentence explaining the modern internet to a traveler from 1800."""

import os

SENTENCE = (
    "One great hall where every book lies open and every voice is heard, and "
    "your letter reaches any town before you lift your pen."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()