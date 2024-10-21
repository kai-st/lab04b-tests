from unittest import TestCase


import Q3


class Test(TestCase):

    def test_shift_letter_is_bound_case_a_with_positive_shift(self):
        actual = Q3.shift_letter("a", 1)
        expected = "b"
        self.assertEqual(expected, actual)

    def test_shift_letter_is_bound_case_A_with_positive_shift(self):
        actual = Q3.shift_letter("A", 1)
        expected = "B"
        self.assertEqual(expected, actual)

    def test_shift_letter_is_bound_case_a_with_negative_shift(self):
        actual = Q3.shift_letter("a", -1)
        expected = "z"
        self.assertEqual(expected, actual)

    def test_shift_letter_is_bound_case_A_with_negative_shift(self):
        actual = Q3.shift_letter("A", -1)
        expected = "Z"
        self.assertEqual(expected, actual)

    def test_shift_letter_is_bound_case_Z_with_positive_shift(self):
        actual = Q3.shift_letter("Z", 1)
        expected = "A"
        self.assertEqual(expected, actual)

    def test_shift_letter_is_bound_case_Z_with_negative_shift(self):
        actual = Q3.shift_letter("Z", -1)
        expected = "Y"
        self.assertEqual(expected, actual)

    def test_shift_letter_is_bound_case_z_with_positive_shift(self):
        actual = Q3.shift_letter("z", 1)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_shift_letter_is_bound_case_z_with_negative_shift(self):
        actual = Q3.shift_letter("z", -1)
        expected = "y"
        self.assertEqual(expected, actual)

    def test_shift_letter_typical_letter_with_positive_shift(self):
        actual = Q3.shift_letter("d", 3)
        expected = "g"
        self.assertEqual(expected, actual)

    def test_shift_letter_typical_letter_with_negative_shift(self):
        actual = Q3.shift_letter("g", -3)
        expected = "d"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_is_bound_case_negative_25(self):
        actual = Q3.shift_letter("a", -25)
        expected = "b"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_is_bound_case_positive_25(self):
        actual = Q3.shift_letter("a", 25)
        expected = "z"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_is_0(self):
        actual = Q3.shift_letter("a", 0)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_is_small_negative(self):
        actual = Q3.shift_letter("c", -2)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_is_medium_negative(self):
        actual = Q3.shift_letter("k", -10)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_is_large_negative(self):
        actual = Q3.shift_letter("z", -23)
        expected = "c"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_is_small_positive(self):
        actual = Q3.shift_letter("a", 2)
        expected = "c"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_is_medium_positive(self):
        actual = Q3.shift_letter("a", 10)
        expected = "k"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_is_large_positive(self):
        actual = Q3.shift_letter("a", 23)
        expected = "x"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_causes_negative_wrap(self):
        actual = Q3.shift_letter("a", -10)
        expected = "q"
        self.assertEqual(expected, actual)

    def test_shift_letter_shift_causes_positive_wrap(self):
        actual = Q3.shift_letter("z", 10)
        expected = "j"
        self.assertEqual(expected, actual)

    def test_shift_letter_capital_letter(self):
        actual = Q3.shift_letter("B", 1)
        expected = "C"
        self.assertEqual(expected, actual)

    def test_shift_letter_lowercase_letter(self):
        actual = Q3.shift_letter("b", 1)
        expected = "c"
        self.assertEqual(expected, actual)
