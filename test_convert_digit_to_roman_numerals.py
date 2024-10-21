from unittest import TestCase


import  Q2


class Test(TestCase):

    def test_convert_digit_to_roman_numerals_digit_is_bound_case_0(self):
        actual = Q2.convert_digit_to_roman_numerals(0, 1)
        expected = ""
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_digit_is_bound_case_9(self):
        actual = Q2.convert_digit_to_roman_numerals(9, 0)
        expected = "IX"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_digit_is_special_case_4(self):
        actual = Q2.convert_digit_to_roman_numerals(4, 0)
        expected = "IV"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_0_low_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(2, 0)
        expected = "II"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_0_mid_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(5, 0)
        expected = "V"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_0_high_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(8, 0)
        expected = "VIII"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_1_low_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(2, 1)
        expected = "XX"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_1_mid_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(5, 1)
        expected = "L"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_1_high_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(8, 1)
        expected = "LXXX"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_2_low_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(2, 2)
        expected = "CC"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_2_mid_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(5, 2)
        expected = "D"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_2_high_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(7, 2)
        expected = "DCC"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_3_digit_is_bound_case_5(self):
        actual = Q2.convert_digit_to_roman_numerals(5, 3)
        expected = "MMMMM"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_3_high_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(4, 3)
        expected = "MMMM"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_3_mid_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(3, 3)
        expected = "MMM"
        self.assertEqual(expected, actual)

    def test_convert_digit_to_roman_numerals_power_of_ten_is_3_low_digit(self):
        actual = Q2.convert_digit_to_roman_numerals(1, 3)
        expected = "M"
        self.assertEqual(expected, actual)



