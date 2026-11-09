# Morse Code Interpreter

Encode text to Morse code and decode it back, from the command line or an interactive prompt.

## Why

A small Python exercise in two-way lookup tables and input validation. The goal was correct round trips: anything encoded decodes back to the same text, and characters Morse can't represent produce an error instead of being dropped silently.

## Usage

Needs Python 3.10+, no dependencies.

```bash
python morse.py encode "Hello World"
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..

python morse.py decode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
# HELLO WORLD

python morse.py            # interactive: type text or Morse, it detects which
```

## Format

- Letters are separated by one space; words by ` / ` (three spaces also work when decoding).
- Supports A–Z, 0–9 and the ITU punctuation set: `. , ? ' ! / ( ) & : ; = + - _ " $ @`
- Output is uppercase, because Morse has no case.
- Unsupported characters or codes are listed in the error and give exit code 1.

## Tests

```bash
python -m unittest -v
```
