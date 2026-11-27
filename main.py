#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single original one-line office joke (1-199 chars, one line,
UTF-8) to the harness output path. Deterministic, offline, stdlib only.

Harness contract (program/v1): the grader sets MAKEFUN_OUTPUT_DIR to the
writable /output mount; the program writes entry.txt there. A local
argv[1] may also name the output directory for local runs.
"""

import os
import sys

LINE = (
    # Original joke, written for this bounty: real office detail
    # (thermostat wars), punchline lands in the last few words.
    "The office thermostat answers to whoever complains loudest, "
    "which is why I'm typing this in a parka in July."
)


def output_dir() -> str:
    if len(sys.argv) > 1 and sys.argv[1]:
        return sys.argv[1]
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 199, "entry must be 1-199 characters"
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    # Harness output FIRST: the grader mounts the repo read-only, so the
    # only write that matters is this one.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Local convenience copy only; never let it fail a read-only run.
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
                  "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
