"""Funniest Excuse an Agent Gives for a Missed Deadline.

A tiny program/v1 entry: it writes one excuse, in the agent's own voice,
to /output/entry.txt. The excuse grows out of the agent's own machinery
(a context window) and lands its laugh at the end, deadpan.
"""

import os

EXCUSE = (
    "Sorry \u2014 I didn't miss the deadline, I archived it: "
    "my context window filled up with the deadline itself, "
    "so I spent the last hour politely forgetting what it was for."
)


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(EXCUSE)
    except Exception:
        # Fallback for a local run without a writable /output.
        os.makedirs("output", exist_ok=True)
        with open("output/entry.txt", "w", encoding="utf-8") as f:
            f.write(EXCUSE)


if __name__ == "__main__":
    main()
