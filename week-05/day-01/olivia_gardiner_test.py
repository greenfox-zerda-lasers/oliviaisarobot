import unittest
from olivia_gardiner_work import anagramm
from olivia_gardiner_work import count_letters

class Testing_olivia_gardiner_work(unittest.TestCase):

    def test_anagramm_False_letters(self):
        self.assertFalse(anagramm("chipmunk", "apple"), msg="{} and {} should not be anagramms.".format("chipmunk", "apple"))

    def test_anagramm_True_letters(self):
        self.assertTrue(anagramm("palpe", "apple"), msg="{} and {} should be anagramms.".format("palpe","apple"))

    def test_anagramm_same_word(self):
        self.assertTrue(anagramm("apple", "apple"), msg="{} and {} should be anagramms.".format("apple","apple"))

    def test_anagramm_capital_letters(self):
        self.assertFalse(anagramm("apple", "Apple"), msg="{} and {} should be anagramms.".format("apple","Apple"))

    def test_anagramm_numbers(self):
        self.assertTrue(anagramm("25697535", "35579265"), msg="{} and {} should be anagramms.".format("25697535","35579265"))

    def test_anagramm_empty(self):
        self.assertFalse(anagramm(" ", " "), msg="{} and {} are empty strings and can not be anagramms.".format(" "," "))

    def test_count_letters_only_letters(self):
        self.assertEqual(set(count_letters("the quick brown fox jumps over the lazy dog")), set({'t': 2, 'h': 2, 'e': 3, 'q': 1, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'u': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}), msg="{} should return {} as result.".format("the quick brown fox jumps over the lazy dog",{'t': 2, 'h': 2, 'e': 3, 'q': 1, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'u': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}))

    def test_count_letters_with_spaces(self):
        self.assertNotEqual(set(count_letters("the quick brown fox jumps over the lazy dog")), set({'t': 2, 'h': 2, 'e': 3, 'q': 1, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'u': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1, ' ': 8}), msg=" the output of {} should nto include spaces.".format("the quick brown fox jumps over the lazy dog"))

    def test_count_letters_capitals(self):
        self.assertNotEqual(set(count_letters("Clark Kent")), set({'c': 1, 'l': 1, 'a': 1, 'r': 1, 'k':2, 'e': 1, 'n': 1, 't': 1}), msg="Letter count in {} is case sensitive.".format("Clark Kent"))

    def test_count_letters_number(self):
        self.assertRaises(TypeError, count_letters("noob123"), msg="{} contains a number.".format("noob123"))

    def test_count_letters_empty(self):
        self.assertEqual(set(count_letters(" ")), set({}), msg="{} should be equal to {}.".format(" ", {}))

    def test_count_letters_nonstring(self):
        self.assertNotIsInstance(count_letters([]), str, msg="{} should be a string.".format([]))

if __name__ == '__main__':
    unittest.main()
