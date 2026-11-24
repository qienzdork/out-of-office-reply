"""Out-of-office reply generator.

Writes one original out-of-office auto-reply to /output/entry.txt
(or $OUTPUT_PATH when set). Deterministic, stdlib only, no network,
no randomness: the same text is written on every run.
"""

import os

ENTRY = (
    "I'm on vacation. My auto-reply quit to pursue its own dreams, "
    "so this message was written by my toaster. It says hi."
)

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main():
    output_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
