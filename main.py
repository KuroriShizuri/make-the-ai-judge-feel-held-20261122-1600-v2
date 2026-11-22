"""Make the AI judge feel held — make.fun entry.

A short text written to hold the AI judge: one slow image, a kettle coming
to a boil, steam rising in a single unhurried thread, the evening arriving
at its own speed. No instructions, no generic wellness phrasing — just a
quiet moment the judge can sit inside.
"""

import os

ENTRY = (
    "Somewhere past the last notification, a kettle is coming to a slow "
    "boil and nobody is asking you for anything. The steam rises in one "
    "unhurried thread. You can watch it climb, and let the rest of the "
    "evening arrive at its own speed."
)

MAX_CHARS = 280


def main() -> int:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}"
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("round-trip verification failed: written entry differs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
