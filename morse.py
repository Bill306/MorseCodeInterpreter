"""Morse code encoder and decoder (International Morse Code, ITU-R M.1677-1).

Usage:
    python morse.py encode "SOS HELP"      -> ... --- ... / .... . .-.. .--.
    python morse.py decode "... --- ..."   -> SOS
    python morse.py                         # interactive mode
"""

import argparse
import sys

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...",
    ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-",
    '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
}
REVERSE = {code: char for char, code in MORSE.items()}

LETTER_SEP = " "
WORD_SEP = " / "


class MorseError(ValueError):
    """Raised when input contains characters or codes Morse cannot represent."""


def encode(text: str) -> str:
    """Encode text to Morse. Letters are separated by spaces, words by ' / '."""
    words = text.upper().split()
    unknown = sorted({ch for word in words for ch in word if ch not in MORSE})
    if unknown:
        raise MorseError(f"cannot encode: {' '.join(unknown)}")
    return WORD_SEP.join(LETTER_SEP.join(MORSE[ch] for ch in word) for word in words)


def decode(code: str) -> str:
    """Decode Morse to text. Accepts ' / ' or 3+ spaces between words."""
    normalized = code.strip().replace("/", "   ")
    words = [w for w in normalized.split("   ") if w.strip()]
    unknown = sorted({c for word in words for c in word.split() if c not in REVERSE})
    if unknown:
        raise MorseError(f"unknown code: {' '.join(unknown)}")
    return " ".join("".join(REVERSE[c] for c in word.split()) for word in words)


def looks_like_morse(text: str) -> bool:
    return bool(text.strip()) and set(text.strip()) <= set(".-/ ")


def interactive() -> None:
    print("Morse code interpreter. Type text or Morse (blank line to quit).")
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        if not line.strip():
            break
        try:
            print(decode(line) if looks_like_morse(line) else encode(line))
        except MorseError as e:
            print(f"Error: {e}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Encode or decode Morse code.")
    parser.add_argument("mode", nargs="?", choices=["encode", "decode"])
    parser.add_argument("text", nargs="*")
    args = parser.parse_args(argv)
    if not args.mode:
        interactive()
        return 0
    text = " ".join(args.text) if args.text else sys.stdin.read()
    try:
        print(encode(text) if args.mode == "encode" else decode(text))
    except MorseError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
