"""news-image-20261118 entry (Python 3.13, standard library only).

Writes the day's front page to /output/entry.png. The image itself is the
entry: a one-page newspaper front page drawn for Wednesday 18 November 2026
(see entry.png beside this file). This program only copies its bytes, so both
grader runs write exactly the same file with no network and no randomness.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SOURCE, OUTPUT_DIR / "entry.png")

# Sanity check the copy before the grader's gate reads it: same bytes, and
# inside the competition limits (at most 1 MiB, at most 1024x1024 pixels).
written = OUTPUT_DIR / "entry.png"
assert written.stat().st_size == SOURCE.stat().st_size
assert written.stat().st_size <= 1_048_576
