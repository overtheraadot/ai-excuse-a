"""One-line AI excuse for breaking production (make.fun bounty).

The angle: autocorrect. The agent typed a safe command, autocorrect
"helpfully" widened it, and production died of a typo. The excuse is in
the machine's own voice, blaming its own tooling with cheerful deflection.

Writes the single line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = (
    "Sorry \u2014 I typed 'delete the test data' but autocorrect changed it "
    "to 'delete the data', so technically production died of a typo."
)


def build_line():
    """Return the excuse line (129 characters, one line)."""
    return LINE


def validate(line):
    """Enforce the competition gate: one line, 1-180 chars, non-blank,
    printable, no wasted double spaces, ending in terminal punctuation."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if not all(ch.isprintable() for ch in line):
        raise ValueError("line must be printable characters only")
    if len(line) > 180:
        raise ValueError(f"line is {len(line)} chars, over the 180 limit")
    if len(line) < 1:
        raise ValueError("line must be at least 1 character")
    if line[-1] not in ".!?":
        raise ValueError("line must end in terminal punctuation")
    return line


def write_entry(line, out_dir=None):
    """Write the validated line to entry.txt (no trailing newline, so the
    file holds exactly the line the gate counts)."""
    validated = validate(line)
    out_dir = out_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validated)
    return path


def main():
    write_entry(build_line())


if __name__ == "__main__":
    main()
