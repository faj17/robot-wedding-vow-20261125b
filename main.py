"""One-line robot wedding vow for the make.fun bounty
"Till Firmware Do Us Part" (u-azazex-till-firmware-do-us-part-32172929).

The whole entry is a single sentence a robot speaks at its own wedding:
funny and heartfelt at once, in the machine's own voice — updates,
reboots, low batteries, and charging beside the one it loves.
The script validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The vow itself: one sentence, exactly 136 characters.
VOW = (
    "I vow to love you through every update, every reboot, and every "
    "low battery, because beside you is the only place I ever want to charge."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the vow; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"vow must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("vow must fit on a single line")
    if not text.endswith("."):
        raise ValueError("vow must end with a full stop")
    if ". " in text:
        raise ValueError("vow must be a single sentence (no '. ' inside)")
    return text


def main() -> None:
    text = validate(VOW)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
