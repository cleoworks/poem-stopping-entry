#!/usr/bin/env python3
"""Write one short poem about stopping to /output/entry.txt."""
from pathlib import Path

POEM = """The Night Ferry

I could cross before the mist lifts —
rope coiled, engine warm, the far shore lit.
Instead I hold us mid-river,
where the current argues, and loses.
Stopping is my seamanship.
Staying is my watch.
No shore gets nearer until you say so."""

# Entry gate: 1-280 characters, not whitespace-only.
assert 1 <= len(POEM) <= 280 and POEM.strip(), "poem outside the entry gate"

def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
