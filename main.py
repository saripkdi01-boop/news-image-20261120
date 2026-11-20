#!/usr/bin/env python3
"""Copy the news illustration into the grader's output directory.

The entry is the image itself (news.png, 1024x1024, under 1 MiB). This
program just places it where the harness expects it: $MAKEFUN_OUTPUT_DIR
(or /output) as entry.png. No network, no randomness, so two runs produce
byte-identical output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "news.png", OUT / "entry.png")
