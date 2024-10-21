from unittest import TestCase


import Q2


class Test(TestCase):

    def test_get_roman_numeral_for_power_of_ten_0(self):
        actual = Q2.get_roman_numeral_for_power_of_ten(0)
        expected = "I"
        self.assertEqual(expected, actual)

    def test_get_roman_numeral_for_power_of_ten_1(self):
        actual = Q2.get_roman_numeral_for_power_of_ten(1)
        expected = "X"
        self.assertEqual(expected, actual)

    def test_get_roman_numeral_for_power_of_ten_2(self):
        actual = Q2.get_roman_numeral_for_power_of_ten(2)
        expected = "C"
        self.assertEqual(expected, actual)

    def test_get_roman_numeral_for_power_of_ten_3(self):
        actual = Q2.get_roman_numeral_for_power_of_ten(3)
        expected = "M"
        self.assertEqual(expected, actual)
