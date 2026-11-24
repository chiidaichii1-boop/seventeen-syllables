"""Write one debugging haiku (5-7-5) to the output directory.

Syllables: 5 / 7 / 5. One concrete picture: log lines scrolling
past midnight, one red line, and the last-line turn — a typo.
"""

import os

# Each line earns its place; the last line turns the poem.
LINES = [
    "Logs scroll past midnight",           # 5: Logs(1) scroll(1) past(1) mid-night(2)
    "one red line breaks the still night",  # 7: one red line breaks the still night
    "it was a typo",                        # 5: it(1) was(1) a(1) ty-po(2)
]

HAIKU = "\n".join(LINES)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
