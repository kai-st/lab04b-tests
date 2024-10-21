from unittest import TestCase


import Q3


class TestCaesarCipher(TestCase):

    def test_caesarcipher_encrypt_message_is_bound_case_z(self):
        actual = Q3.caesarcipher("z", True, -1)
        expected = "y"
        self.assertEqual(expected, actual)

    def test_caesarcipher_decrypt(self):
        actual = Q3.caesarcipher("b", False, 1)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_encode_is_false_with_negative_shift(self):
        first_pass = Q3.caesarcipher("cat", True, -1)
        actual = Q3.caesarcipher(first_pass, False, -1)
        expected = "cat"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_encode_is_true_with_negative_shift(self):
        first_pass = Q3.caesarcipher("cat", False, -1)
        actual = Q3.caesarcipher(first_pass, True, -1)
        expected = "cat"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_encode_is_balanced(self):
        first_pass = Q3.caesarcipher("cat", True, 1)
        actual = Q3.caesarcipher(first_pass, False, 1)
        expected = "cat"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_decode_is_balanced(self):
        first_pass = Q3.caesarcipher("cat", False, 1)
        actual = Q3.caesarcipher(first_pass, True, 1)
        expected = "cat"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_0(self):
        actual = Q3.caesarcipher("a", True, 0)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_small_negative(self):
        actual = Q3.caesarcipher("a", True, -1)
        expected = "z"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_medium_negative(self):
        actual = Q3.caesarcipher("a", True, -10)
        expected = "q"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_large_negative(self):
        actual = Q3.caesarcipher("a", True, -25)
        expected = "b"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_huge_negative(self):
        actual = Q3.caesarcipher("a", True, -999)
        expected = "p"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_small_positive(self):
        actual = Q3.caesarcipher("a", True, 1)
        expected = "b"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_medium_positive(self):
        actual = Q3.caesarcipher("a", True, 10)
        expected = "k"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_large_positive(self):
        actual = Q3.caesarcipher("a", True, 25)
        expected = "z"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_huge_positive(self):
        actual = Q3.caesarcipher("a", True, 999)
        expected = "l"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_positive_cycle(self):
        actual = Q3.caesarcipher("a", True, 26)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_shift_is_negative_cycle(self):
        actual = Q3.caesarcipher("a", True, -26)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_empty(self):
        actual = Q3.caesarcipher("", True, 1)
        expected = ""
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_all_capital(self):
        actual = Q3.caesarcipher("AAA", True, 1)
        expected = "BBB"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_upper_and_lower(self):
        actual = Q3.caesarcipher("Aa", True, 1)
        expected = "Bb"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_all_spaces(self):
        actual = Q3.caesarcipher(" ", True, 1)
        expected = " "
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_short_message(self):
        actual = Q3.caesarcipher("hi", True, 1)
        expected = "ij"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_large_message(self):
        actual = Q3.caesarcipher("Supercalifragilisticexpialidocious", True, 1)
        expected = "Tvqfsdbmjgsbhjmjtujdfyqjbmjepdjpvt"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_all_lower_case(self):
        actual = Q3.caesarcipher("abc", True, 1)
        expected = "bcd"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_bound_case_a(self):
        actual = Q3.caesarcipher("a", True, 1)
        expected = "b"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_bound_case_Z(self):
        actual = Q3.caesarcipher("Z", True, 1)
        expected = "A"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_bound_case_A(self):
        actual = Q3.caesarcipher("A", True, 1)
        expected = "B"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_bound_case_with_punctuation(self):
        actual = Q3.caesarcipher("A.a.Z.z.", True, 1)
        expected = "B.b.A.a."
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_typical_value(self):
        actual = Q3.caesarcipher("hello, world.", True, 1)
        expected = "ifmmp, xpsme."
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_is_length_one(self):
        actual = Q3.caesarcipher("a", True, 1)
        expected = "b"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_with_white_space(self):
        actual = Q3.caesarcipher("hello world", True, 1)
        expected = "ifmmp xpsme"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_with_numbers(self):
        actual = Q3.caesarcipher("hello12", True, 1)
        expected = "ifmmp12"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_with_symbols(self):
        actual = Q3.caesarcipher("hello!", True, 1)
        expected = "ifmmp!"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_with_punctuation(self):
        actual = Q3.caesarcipher("hello, world!", True, 1)
        expected = "ifmmp, xpsme!"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_with_just_numbers(self):
        actual = Q3.caesarcipher("123", True, 1)
        expected = "123"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_with_just_symbols(self):
        actual = Q3.caesarcipher("#$%", True, 1)
        expected = "#$%"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_with_just_escape_character(self):
        actual = Q3.caesarcipher("123\t123", True, 1)
        expected = "123\t123"
        self.assertEqual(expected, actual)

    def test_caesarcipher_encrypt_message_all_punctuation(self):
        actual = Q3.caesarcipher(",.,", True, 1)
        expected = ",.,"
        self.assertEqual(expected, actual)
