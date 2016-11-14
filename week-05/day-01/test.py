import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(2, 3), 5)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(4, 1), 5)

    def test_add_4_and_2_is_5(self):
        self.assertNotEqual(extend.add(4, 2), 5)

    def test_add_apple_and_lemon_is_5(self):
        self.assertNotIsInstance(extend.add('apple', 'lemon'), int)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 4, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(3, 4, 5), 5)

    def test_max_of_three_second(self):
        self.assertEqual(extend.max_of_three(3, 5, 4), 5)

    def test_max_of_three_strings(self):
        self.assertRaises(TypeError, extend.max_of_three("duck", "hedgehog", "kiwi"))

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,5]), 5)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5]), 2.5)

    def test_median_three(self):
        self.assertEqual(extend.median([1,2,4,3]), 3)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))

    def test_is_vovel_longu(self):
        self.assertTrue(extend.is_vovel('ú'))

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

    def test_translate_kolbice(self):
        self.assertRaises(TypeError, extend.translate('kol123bice'))

if __name__ == '__main__':
    unittest.main()
