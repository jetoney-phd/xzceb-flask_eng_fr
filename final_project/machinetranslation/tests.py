"""
Unit tests for English-French and French-English functions
"""
import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):

    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

        self.assertNotEqual(english_to_french('Goodbye'), 'Bonjour')

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

        self.assertNotEqual(french_to_english('Au revoir'), 'Hello')

if __name__ == '__main__':
    unittest.main()
