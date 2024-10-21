from unittest import TestCase


import Q1


class Test(TestCase):

    def test_convert_decimal_to_base_decimal_is_0(self):
        actual = Q1.convert_decimal_to_base(0, 6)
        expected = "0"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_decimal_less_than_base(self):
        actual = Q1.convert_decimal_to_base(2, 6)
        expected = "2"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_decimal_greater_than_base(self):
        actual = Q1.convert_decimal_to_base(6, 2)
        expected = "110"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_decimal_equals_base(self):
        actual = Q1.convert_decimal_to_base(6, 6)
        expected = "10"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_is_bound_case_base_2(self):
        actual = Q1.convert_decimal_to_base(25, 2)
        expected = "11001"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_is_bound_case_base_9(self):
        actual = Q1.convert_decimal_to_base(25, 9)
        expected = "27"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_mid_base(self):
        actual = Q1.convert_decimal_to_base(25, 4)
        expected = "121"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_small_decimal_power_of_base(self):
        actual = Q1.convert_decimal_to_base(9, 3)
        expected = "100"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_small_decimal_not_power_of_base(self):
        actual = Q1.convert_decimal_to_base(10, 2)
        expected = "1010"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_medium_decimal_power_of_base(self):
        actual = Q1.convert_decimal_to_base(343, 7)
        expected = "1000"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_medium_decimal_not_power_of_base(self):
        actual = Q1.convert_decimal_to_base(102, 5)
        expected = "402"
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_large_decimal_power_of_base(self):
        actual = Q1.convert_decimal_to_base(5 ** 50, 5)
        expected = "1" + "0" * 50
        self.assertEqual(expected, actual)

    def test_convert_decimal_to_base_large_decimal_not_power_of_base(self):
        actual = Q1.convert_decimal_to_base(8 ** 50 + 1, 8)
        expected = "1" + "0" * (50 - 1) + "1"
        self.assertEqual(expected, actual)
