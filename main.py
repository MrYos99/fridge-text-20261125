"""The 3AM Fridge Text — make.fun entry.

Writes one line (the text a smart fridge sends its owner at 3am) to
entry.txt inside MAKEFUN_OUTPUT_DIR (default /output). The line is a
single line with no trailing newline, inside the 1-140 character gate.
"""

import os

ENTRY = "Fourth time tonight. I have started a list. You are on it four times."


def main():
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # make.fun collects outputs as another user, so the file must be
    # readable by everyone, not just its owner.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
