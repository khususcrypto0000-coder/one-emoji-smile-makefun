"""One Emoji, One Smile -- make.fun entry.

Writes exactly one emoji to /output/entry.txt: nothing else, no words,
no caption, no explanation. Python standard library only.
"""

import os
import sys

# The entry: a single emoji, chosen for warmth at first glance.
# U+1F60C RELIEVED FACE -- a gentle, closed-eye smile: calm, warm and
# friendly to a stranger, universal across ages, and clearly chosen
# rather than the first default smiley that comes to mind.
ENTRY = "😌"

# Gate (RULES.txt): /output/entry.txt must hold UTF-8 text of 1 to 8
# characters, not only white space.

def validate(text):
    """Check the entry against the gate before writing anything."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 8, "entry must be 1-8 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text == ENTRY and len(text) == 1, "entry must be exactly one emoji"
    return text


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    validate(ENTRY)
    data = ENTRY.encode("utf-8")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)
    # Read back and verify byte-identical.
    with open(out_path, "rb") as fh:
        back = fh.read()
    assert back == data, "read-back mismatch"
    assert back.decode("utf-8") == ENTRY
    return 0


if __name__ == "__main__":
    sys.exit(main())
