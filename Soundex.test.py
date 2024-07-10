import unittest
from Soundex import generate_soundex
class TestSoundex(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")
    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
    def test_simple_cases(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Rubin"), "R150")
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Ashcroft"), "A261")
        self.assertEqual(generate_soundex("Pfister"), "P236")    
if __name__ == '__main__':
    unittest.main()
