"""Copy the pre-rendered news image to the grader's output path.

The entry image (news.png) is a front-page summary of the world's news of
Monday 23 November 2026, rendered at build time. This program only places a
byte-for-byte copy at the output location the grader reads.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Fail loudly instead of silently shipping a truncated copy.
    if os.path.getsize(dst) != os.path.getsize(SRC):
        raise SystemExit("entry.png size mismatch after copy")


if __name__ == "__main__":
    main()
