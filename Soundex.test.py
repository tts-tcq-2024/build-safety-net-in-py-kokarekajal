import unittest

def generate_soundex(name):
    """Simple placeholder implementation for the Soundex algorithm."""
    if not name:
        return ""
    name = name.upper()
    soundex = name[0]
    digits = "01230120022455012623010202"
    for char in name[1:]:
        num = digits[ord(char) - ord('A')]
        if num != '0':
            soundex += num
    soundex = soundex[:4].ljust(4, '0')
    return soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_simple_name(self):
        self.assertEqual(generate_soundex("Smith"), "S530")

    def test_ignore_vowels_and_specific_consonants(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")

    def test_handle_same_letter_repetition(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")

    def test_handle_non_alpha_characters(self):
        self.assertEqual(generate_soundex("McDonald"), "M235")

    def test_handle_name_with_spaces(self):
        self.assertEqual(generate_soundex("Van Helsing"), "V542")

    def test_handle_name_with_punctuation(self):
        self.assertEqual(generate_soundex("O'Connor"), "O256")

if __name__ == '__main__':
    unittest.main()
