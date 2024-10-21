from unittest import TestCase


import Q2


class Test(TestCase):

    def test_convert_arabic_to_roman_numeral_is_bound_case_1(self):
        actual = Q2.convert_arabic_to_roman_numeral("1")
        expected = "I"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_is_bound_case_5000(self):
        actual = Q2.convert_arabic_to_roman_numeral("5000")
        expected = "MMMMM"
        self.assertEqual(expected, actual)


    def test_convert_arabic_to_roman_numeral_single_digit_bottom_bound_1(self):
        actual = Q2.convert_arabic_to_roman_numeral("1")
        expected = "I"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_low_single_digit(self):
        actual = Q2.convert_arabic_to_roman_numeral("2")
        expected = "II"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_mid_single_digit(self):
        actual = Q2.convert_arabic_to_roman_numeral("5")
        expected = "V"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_high_single_digit(self):
        actual = Q2.convert_arabic_to_roman_numeral("8")
        expected = "VIII"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_single_digit_top_bound_9(self):
        actual = Q2.convert_arabic_to_roman_numeral("9")
        expected = "IX"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_double_digits_bottom_bound_10(self):
        actual = Q2.convert_arabic_to_roman_numeral("10")
        expected = "X"
        self.assertEqual(expected, actual)
        
    def test_convert_arabic_to_roman_numeral_low_double_digits(self):
        actual = Q2.convert_arabic_to_roman_numeral("26")
        expected = "XXVI"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_mid_double_digits(self):
        actual = Q2.convert_arabic_to_roman_numeral("50")
        expected = "L"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_high_double_digits(self):
        actual = Q2.convert_arabic_to_roman_numeral("84")
        expected = "LXXXIV"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_double_digits_top_bound_99(self):
        actual = Q2.convert_arabic_to_roman_numeral("99")
        expected = "XCIX"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_triple_digits_bottom_bound_100(self):
        actual = Q2.convert_arabic_to_roman_numeral("100")
        expected = "C"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_low_triple_digits(self):
        actual = Q2.convert_arabic_to_roman_numeral("343")
        expected = "CCCXLIII"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_mid_triple_digits(self):
        actual = Q2.convert_arabic_to_roman_numeral("500")
        expected = "D"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_high_triple_digits(self):
        actual = Q2.convert_arabic_to_roman_numeral("705")
        expected = "DCCV"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_triple_digits_top_bound_999(self):
        actual = Q2.convert_arabic_to_roman_numeral("999")
        expected = "CMXCIX"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_quadruple_digits_bottom_bound_1000(self):
        actual = Q2.convert_arabic_to_roman_numeral("1000")
        expected = "M"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_low_quadruple_digits(self):
        actual = Q2.convert_arabic_to_roman_numeral("2011")
        expected = "MMXI"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_mid_quadruple_digits(self):
        actual = Q2.convert_arabic_to_roman_numeral("3400")
        expected = "MMMCD"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_high_quadruple_digits(self):
        actual = Q2.convert_arabic_to_roman_numeral("4999")
        expected = "MMMMCMXCIX"
        self.assertEqual(expected, actual)

    def test_convert_arabic_to_roman_numeral_quadruple_digits_top_bound_5000(self):
        actual = Q2.convert_arabic_to_roman_numeral("5000")
        expected = "MMMMM"
        self.assertEqual(expected, actual)
    

