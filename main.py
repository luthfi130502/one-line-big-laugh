"""One Line, Big Laugh — writes a single funny line to /output/entry.txt.

The line is a self-own about phone security: the setup lists three ways
in, then the turn reveals the owner locked himself out of all of them.
The program checks the gate itself (one line, 1-200 chars) before writing.
"""

import os

LINE = (
    "My phone now unlocks with my face, my fingerprint, and a six-digit code — "
    "and I still can't get in, because I changed all three after the breakup "
    "and forgot to tell myself."
)


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
