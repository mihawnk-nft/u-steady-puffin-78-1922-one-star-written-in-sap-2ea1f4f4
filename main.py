"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

Pure Python standard library. Deterministic: the same text on every run,
so both graded runs of the program produce the same entry.
"""

import os

# The review: 166 characters, one line, under the 280-character cap.
# Grievance: the owner waters the plastic succulent next to the plant
# twice a week while the real plant dies of thirst one pot over —
# and the fake plant is outliving it.
REVIEW_PARTS = (
    "One star. She waters the plastic succulent next to me twice a week ",
    "and calls me 'low-maintenance' while I die of thirst one pot over. ",
    "The plastic one is outliving me.",
)


def build_review() -> str:
    """Assemble the review line from its fixed parts."""
    return "".join(REVIEW_PARTS).strip()


def resolve_output_path() -> str:
    """Output path: OUTPUT_DIR env override, else the grader's default."""
    return os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def validate(text: str) -> None:
    """Enforce the competition's length and non-blank rules."""
    if not (1 <= len(text) <= 279):
        raise SystemExit(
            "review must be 1-279 characters, got %d" % len(text)
        )
    if not text.strip():
        raise SystemExit("review must not be only whitespace")


def main() -> None:
    text = build_review()
    validate(text)
    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
