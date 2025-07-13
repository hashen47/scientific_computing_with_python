import string, unittest
from typing import List
from constraint_pair import ConstraintPair
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def compare_digit_count(self, password: str, min_digit_count: int) -> bool:
        digit_count: int = 0 
        for password_ch in password:
            for ch in string.digits:
                if password_ch == ch:
                    digit_count += 1
        return min_digit_count <= digit_count

    def compare_lowercase_count(self, password: str, min_lowercase_count: int) -> bool:
        lowercase_count: int = 0 
        for password_ch in password:
            for ch in string.ascii_lowercase:
                if password_ch == ch:
                    lowercase_count += 1
        return min_lowercase_count <= lowercase_count

    def compare_uppercase_count(self, password: str, min_uppercase_count: int) -> bool:
        uppercase_count: int = 0 
        for password_ch in password:
            for ch in string.ascii_uppercase:
                if password_ch == ch:
                    uppercase_count += 1
        return min_uppercase_count <= uppercase_count

    def compare_symbol_count(self, password: str, min_symbol_count: int) -> bool:
        symbol_count: int = 0 
        for password_ch in password:
            for ch in string.punctuation:
                if password_ch == ch:
                    symbol_count += 1
        return min_symbol_count <= symbol_count

    def test_generate_password(self):
        class Testcase:
            def __init__(self, length: str, digit_count: str, lowercase_count: str, uppercase_count: str, symbol_count: str, length_error: str = "", digit_count_error: str = "", lowercase_count_error: str = "", uppercase_count_error: str = "", symbol_count_error: str = ""):
                self.length: str = length
                self.digit_count: str = digit_count
                self.lowercase_count: str = lowercase_count
                self.uppercase_count: str = uppercase_count
                self.symbol_count: str = symbol_count
                self.length_error: str = length_error
                self.digit_count_error: str = digit_count_error
                self.lowercase_count_error: str = lowercase_count_error
                self.uppercase_count_error: str = uppercase_count_error
                self.symbol_count_error: str = symbol_count_error

        testcases: List[Testcase] = [
            Testcase("8", "1", "1", "1", "1"),
            Testcase("16", "1", "1", "1", "1"),
            Testcase("1", "0", "0", "0", "0"),
            Testcase("32", "20", "1", "1", "1"),
            Testcase("32", "29", "1", "1", "1"),
            Testcase("60", "30", "20", "9", "1"),
            Testcase("60.23432", "30.2342", "20.234", "9.2342", "1.234"),

            Testcase("0", "30", "20", "9", "1", length_error="ERROR: password length cannot be zero or negative: 0"),
            Testcase("-1", "30", "20", "9", "1", length_error="ERROR: password length cannot be zero or negative: -1"),
            Testcase("-1.234324", "30", "20", "9", "1", length_error="ERROR: password length cannot be zero or negative: -1"),
            Testcase("-0.234324", "30", "20", "9", "1", length_error="ERROR: password length cannot be zero or negative: 0"),
            Testcase("asdfsdfsfsd", "30", "20", "9", "1", length_error="ERROR: invalid integer value: asdfsdfsfsd"),
            Testcase("-1234.1324414basdfsdfsfsd", "30", "20", "9", "1", length_error="ERROR: invalid integer value: -1234.1324414basdfsdfsfsd"),

            Testcase("100", "0", "20", "9", "1"),
            Testcase("100", "-30", "20", "9", "1", digit_count_error="ERROR: digit count cannot be negative: -30"),
            Testcase("200", "-30.234324", "20", "9", "1", digit_count_error="ERROR: digit count cannot be negative: -30"),
            Testcase("300", "basdfsdfsfsd", "20", "9", "1", digit_count_error="ERROR: invalid integer value: basdfsdfsfsd"),
            Testcase("100", "-1234.1324414basdfsdfsfsd", "20", "9", "1", digit_count_error="ERROR: invalid integer value: -1234.1324414basdfsdfsfsd"),
            Testcase("40", "30.234sfds", "20", "9", "1", digit_count_error="ERROR: invalid integer value: 30.234sfds"),

            Testcase("100", "20", "0", "9", "1"),
            Testcase("100", "20", "-30", "9", "1", lowercase_count_error="ERROR: lowercase character count cannot be negative: -30"),
            Testcase("200", "20", "-30.234324", "9", "1", lowercase_count_error="ERROR: lowercase character count cannot be negative: -30"),
            Testcase("300", "20", "basdfsdfsfsd", "9", "1", lowercase_count_error="ERROR: invalid integer value: basdfsdfsfsd"),
            Testcase("100", "20", "-1234.1324414basdfsdfsfsd", "9", "1", lowercase_count_error="ERROR: invalid integer value: -1234.1324414basdfsdfsfsd"),
            Testcase("40", "20", "30.234sfds", "9", "1", lowercase_count_error="ERROR: invalid integer value: 30.234sfds"),

            Testcase("100", "20", "9", "0", "1"),
            Testcase("100", "20", "9", "-30", "1", uppercase_count_error="ERROR: uppercase character count cannot be negative: -30"),
            Testcase("200", "20", "9", "-30.234324", "1", uppercase_count_error="ERROR: uppercase character count cannot be negative: -30"),
            Testcase("300", "20", "9", "basdfsdfsfsd", "1", uppercase_count_error="ERROR: invalid integer value: basdfsdfsfsd"),
            Testcase("100", "20", "9", "-1234.1324414basdfsdfsfsd", "1", uppercase_count_error="ERROR: invalid integer value: -1234.1324414basdfsdfsfsd"),
            Testcase("40", "20", "9", "30.234sfds", "1", uppercase_count_error="ERROR: invalid integer value: 30.234sfds"),

            Testcase("100", "20", "9", "1", "0"),
            Testcase("100", "20", "9", "1", "-30", symbol_count_error="ERROR: symbol character count cannot be negative: -30"),
            Testcase("200", "20", "9", "1", "-30.234324", symbol_count_error="ERROR: symbol character count cannot be negative: -30"),
            Testcase("300", "20", "9", "1", "basdfsdfsfsd", symbol_count_error="ERROR: invalid integer value: basdfsdfsfsd"),
            Testcase("100", "20", "9", "1", "-1234.1324414basdfsdfsfsd", symbol_count_error="ERROR: invalid integer value: -1234.1324414basdfsdfsfsd"),
            Testcase("40", "20", "9", "1", "30.234sfds", symbol_count_error="ERROR: invalid integer value: 30.234sfds"),
        ]

        for testcase in testcases:
            constraintPair: ConstraintPair = ConstraintPair()

            if constraintPair.set_length(testcase.length):
                self.assertEqual(int(float(testcase.length)), constraintPair.length)
            else:
                self.assertEqual(testcase.length_error, constraintPair.get_error_msg())

            if constraintPair.set_digit_count(testcase.digit_count):
                self.assertEqual(int(float(testcase.digit_count)), constraintPair.min_digit_count)
            else:
                self.assertEqual(testcase.digit_count_error, constraintPair.get_error_msg())

            if constraintPair.set_lowercase_count(testcase.lowercase_count):
                self.assertEqual(int(float(testcase.lowercase_count)), constraintPair.min_lowercase_count)
            else:
                self.assertEqual(testcase.lowercase_count_error, constraintPair.get_error_msg())

            if constraintPair.set_uppercase_count(testcase.uppercase_count):
                self.assertEqual(int(float(testcase.uppercase_count)), constraintPair.min_uppercase_count)
            else:
                self.assertEqual(testcase.uppercase_count_error, constraintPair.get_error_msg())

            if constraintPair.set_symbol_count(testcase.symbol_count):
                self.assertEqual(int(float(testcase.symbol_count)), constraintPair.min_symbol_count)
            else:
                self.assertEqual(testcase.symbol_count_error, constraintPair.get_error_msg())

            try:
                password: str = generate_password(constraintPair)
                if testcase.length_error == "":
                    self.assertEqual(int(float(testcase.length)), len(password))

                if testcase.digit_count_error == "":
                    self.assertEqual(True, self.compare_digit_count(password, int(float(testcase.digit_count))))

                if testcase.lowercase_count_error == "":
                    self.assertEqual(True, self.compare_lowercase_count(password, int(float(testcase.lowercase_count))))

                if testcase.uppercase_count_error == "":
                    self.assertEqual(True, self.compare_uppercase_count(password, int(float(testcase.uppercase_count))))

                if testcase.symbol_count_error == "":
                    self.assertEqual(True, self.compare_symbol_count(password, int(float(testcase.symbol_count))))
            except Exception as e:
                self.assertEqual(str(e), f"ERROR: constraint combine length cannot exceed password length, password length: {constraintPair.length}, constraints length: {constraintPair.get_constraints_length()}")
