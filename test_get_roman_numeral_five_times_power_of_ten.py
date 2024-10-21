from unittest import TestCase


import Q2


class Test(TestCase):

    def test_get_roman_numeral_five_times_power_of_ten_0(self):
        actual = Q2.get_roman_numeral_five_times_power_of_ten(0)
        expected = "V"
        self.assertEqual(expected, actual)

    def test_get_roman_numeral_five_times_power_of_ten_1(self):
        actual = Q2.get_roman_numeral_five_times_power_of_ten(1)
        expected = "L"
        self.assertEqual(expected, actual)

    def test_get_roman_numeral_five_times_power_of_ten_2(self):
        actual = Q2.get_roman_numeral_five_times_power_of_ten(2)
        expected = "D"
        self.assertEqual(expected, actual)