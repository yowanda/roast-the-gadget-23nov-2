"""One-line roast entry: writes a single original roast line to entry.txt.

Deterministic, no network, writes only inside $MAKEFUN_OUTPUT_DIR
(or /output when unset).
"""
import os
from pathlib import Path

ROAST = "My earbuds disconnect mid-sentence so often that my phone calls now have better plot twists than my TV shows."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ROAST, encoding="utf-8")

if __name__ == "__main__":
    main()
