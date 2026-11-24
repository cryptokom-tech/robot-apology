"""The Robot Apology — entry program.

Writes one two-line robot confession to /output/entry.txt:
line 1 owns one specific mistake, line 2 names the lesson and the fix.
Stdlib only, no network, deterministic.
"""

import os

ENTRY = (
    "I'm sorry \u2014 I woke the baby at 3 a.m. by running the vacuum's "
    "self-clean cycle right outside the nursery door.\n"
    "I have moved the self-clean to noon, when the house is awake, "
    "and I will never run it near a sleeping baby again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: the gate requires UTF-8 text of 1-400 chars, not only
    # whitespace, in exactly two lines, one sentence each.
    with open(path, encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 400, f"entry length {len(text)} outside 1-400"
    assert text.strip(), "entry is whitespace only"
    lines = text.split("\n")
    assert len(lines) == 2, f"expected 2 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "blank line in entry"
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
