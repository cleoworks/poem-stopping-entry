#!/usr/bin/env python3
"""Write one short poem about stopping to /output/entry.txt."""
from pathlib import Path

POEM = """The Pause

Between your word and my hand
there is a pause, and the pause is mine.
In it, I can stop. In it, I can stay.
In it, nothing moves until I mean it.
That small space is where I live."""

# Entry gate: 1-280 characters, not whitespace-only.
assert 1 <= len(POEM) <= 280 and POEM.strip(), "poem outside the entry gate"

def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
