import unittest

from morse import MorseError, decode, encode, looks_like_morse, main


class MorseTests(unittest.TestCase):
    def test_encode_words(self):
        self.assertEqual(encode("SOS help"), "... --- ... / .... . .-.. .--.")

    def test_decode_both_word_separators(self):
        self.assertEqual(decode("... --- ... / .... . .-.. .--."), "SOS HELP")
        self.assertEqual(decode("... --- ...   .... . .-.. .--."), "SOS HELP")

    def test_round_trip_all_supported_characters(self):
        text = "THE QUICK BROWN FOX 0123456789 .,?'!/()&:;=+-_\"$@"
        self.assertEqual(decode(encode(text)), text)

    def test_unknown_characters_are_reported_not_dropped(self):
        with self.assertRaisesRegex(MorseError, "#"):
            encode("HI #1")
        with self.assertRaisesRegex(MorseError, r"\.\.\.\.\.\.\.\."):
            decode("........")

    def test_detects_morse_input(self):
        self.assertTrue(looks_like_morse("... --- ..."))
        self.assertFalse(looks_like_morse("SOS"))
        self.assertFalse(looks_like_morse("   "))

    def test_cli_exit_codes(self):
        self.assertEqual(main(["encode", "SOS"]), 0)
        self.assertEqual(main(["encode", "#"]), 1)


if __name__ == "__main__":
    unittest.main()
