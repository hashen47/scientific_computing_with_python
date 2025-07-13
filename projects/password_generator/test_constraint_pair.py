import unittest
from typing import List, Optional
from constraint_pair import ConstraintPair

class TestConstraintPair(unittest.TestCase):
    def setUp(self):
        self.constraintPair: ConstraintPair = ConstraintPair()

    def test_str_to_int(self):
        class TestCase:
            def __init__(self, input: str, output: Optional[int], is_error: bool, error: str):
                self.input: str = input
                self.output: Optional[int] = output
                self.is_error: bool = is_error
                self.error: str = error
        
        testcases: List[TestCase] = [
            TestCase("0", 0, False, ""),
            TestCase("1", 1, False, ""),
            TestCase("         1 ", 1, False, ""),
            TestCase("23243", 23243, False, ""),
            TestCase("23243.23432", 23243, False, ""),
            TestCase("-23243", -23243, False, ""),
            TestCase("-23243.23", -23243, False, ""),
            TestCase("     -23243.23 ", -23243, False, ""),
            TestCase("sdfasfdsfa", None, True, "ERROR: invalid integer value: sdfasfdsfa"),
            TestCase("sdfasfdsfa23432432", None, True, "ERROR: invalid integer value: sdfasfdsfa23432432"),
            TestCase("-sdfasfdsfa23432432", None, True, "ERROR: invalid integer value: -sdfasfdsfa23432432"),
            TestCase("", None, True, "ERROR: number value cannot be empty"),
            TestCase(" "*5, None, True, "ERROR: number value cannot be empty"),
            TestCase(" "*50, None, True, "ERROR: number value cannot be empty"),
            TestCase("  1 234324", None, True, "ERROR: invalid integer value:   1 234324"),
            TestCase("  1 234324 ", None, True, "ERROR: invalid integer value:   1 234324 "),
        ]

        for testcase in testcases:
            self.assertEqual(testcase.output, self.constraintPair.str_to_int(testcase.input))
            if testcase.is_error:
                self.assertEqual(testcase.error, self.constraintPair.get_error_msg())

    def test_set_length(self):
        class TestCase:
            def __init__(self, input: str, output: bool, actual_value: int, is_error: bool, error: str):
                self.input: str = input 
                self.output: bool = output
                self.actual_value: int = actual_value
                self.is_error: bool = is_error
                self.error: str = error

        testcases: List[TestCase] = [
            TestCase("1", True, 1, False, ""),
            TestCase("2", True, 2, False, ""),
            TestCase("3", True, 3, False, ""),
            TestCase("30000", True, 30000, False, ""),
            TestCase("0", False, 0, True, f"ERROR: password length cannot be zero or negative: 0"),
            TestCase("-234", False, 0, True, f"ERROR: password length cannot be zero or negative: -234"),
            TestCase("-234.23423", False, 0, True, f"ERROR: password length cannot be zero or negative: -234"),
            TestCase("234wrong_text", False, 0, True, f"ERROR: invalid integer value: 234wrong_text"),
            TestCase("wwwww234242fsdf!@#$!$#!", False, 0, True, f"ERROR: invalid integer value: wwwww234242fsdf!@#$!$#!"),
            TestCase("", False, 0, True, f"ERROR: number value cannot be empty"),
            TestCase("  ", False, 0, True, f"ERROR: number value cannot be empty"),
        ]

        for testcase in testcases:
            self.assertEqual(testcase.output, self.constraintPair.set_length(testcase.input))
            if testcase.is_error:
                self.assertEqual(testcase.error, self.constraintPair.get_error_msg())
            else:
                self.assertEqual(testcase.actual_value, self.constraintPair.length)

    def test_set_digit_count(self):
        class TestCase:
            def __init__(self, input: str, output: bool, actual_value: int, is_error: bool, error: str):
                self.input: str = input 
                self.output: bool = output
                self.actual_value: int = actual_value
                self.is_error: bool = is_error
                self.error: str = error

        testcases: List[TestCase] = [
            TestCase("1", True, 1, False, ""),
            TestCase("2", True, 2, False, ""),
            TestCase("3", True, 3, False, ""),
            TestCase("30000", True, 30000, False, ""),
            TestCase("-1", False, 0, True, f"ERROR: digit count cannot be negative: -1"),
            TestCase("-234", False, 0, True, f"ERROR: digit count cannot be negative: -234"),
            TestCase("-234.23423", False, 0, True, f"ERROR: digit count cannot be negative: -234"),
            TestCase("234wrong_text", False, 0, True, f"ERROR: invalid integer value: 234wrong_text"),
            TestCase("wwwww234242fsdf!@#$!$#!", False, 0, True, f"ERROR: invalid integer value: wwwww234242fsdf!@#$!$#!"),
            TestCase("", False, 0, True, f"ERROR: number value cannot be empty"),
            TestCase("  ", False, 0, True, f"ERROR: number value cannot be empty"),
        ]

        for testcase in testcases:
            self.assertEqual(testcase.output, self.constraintPair.set_digit_count(testcase.input))
            if testcase.is_error:
                self.assertEqual(testcase.error, self.constraintPair.get_error_msg())
            else:
                self.assertEqual(testcase.actual_value, self.constraintPair.min_digit_count)

    def test_set_lowercase_count(self):
        class TestCase:
            def __init__(self, input: str, output: bool, actual_value: int, is_error: bool, error: str):
                self.input: str = input 
                self.output: bool = output
                self.actual_value: int = actual_value
                self.is_error: bool = is_error
                self.error: str = error

        testcases: List[TestCase] = [
            TestCase("1", True, 1, False, ""),
            TestCase("2", True, 2, False, ""),
            TestCase("3", True, 3, False, ""),
            TestCase("30000", True, 30000, False, ""),
            TestCase("-1", False, 0, True, f"ERROR: lowercase character count cannot be negative: -1"),
            TestCase("-234", False, 0, True, f"ERROR: lowercase character count cannot be negative: -234"),
            TestCase("-234.23423", False, 0, True, f"ERROR: lowercase character count cannot be negative: -234"),
            TestCase("234wrong_text", False, 0, True, f"ERROR: invalid integer value: 234wrong_text"),
            TestCase("wwwww234242fsdf!@#$!$#!", False, 0, True, f"ERROR: invalid integer value: wwwww234242fsdf!@#$!$#!"),
            TestCase("", False, 0, True, f"ERROR: number value cannot be empty"),
            TestCase("  ", False, 0, True, f"ERROR: number value cannot be empty"),
        ]

        for testcase in testcases:
            self.assertEqual(testcase.output, self.constraintPair.set_lowercase_count(testcase.input))
            if testcase.is_error:
                self.assertEqual(testcase.error, self.constraintPair.get_error_msg())
            else:
                self.assertEqual(testcase.actual_value, self.constraintPair.min_lowercase_count)

    def test_set_uppercase_count(self):
        class TestCase:
            def __init__(self, input: str, output: bool, actual_value: int, is_error: bool, error: str):
                self.input: str = input 
                self.output: bool = output
                self.actual_value: int = actual_value
                self.is_error: bool = is_error
                self.error: str = error

        testcases: List[TestCase] = [
            TestCase("1", True, 1, False, ""),
            TestCase("2", True, 2, False, ""),
            TestCase("3", True, 3, False, ""),
            TestCase("30000", True, 30000, False, ""),
            TestCase("-1", False, 0, True, f"ERROR: uppercase character count cannot be negative: -1"),
            TestCase("-234", False, 0, True, f"ERROR: uppercase character count cannot be negative: -234"),
            TestCase("-234.23423", False, 0, True, f"ERROR: uppercase character count cannot be negative: -234"),
            TestCase("234wrong_text", False, 0, True, f"ERROR: invalid integer value: 234wrong_text"),
            TestCase("wwwww234242fsdf!@#$!$#!", False, 0, True, f"ERROR: invalid integer value: wwwww234242fsdf!@#$!$#!"),
            TestCase("", False, 0, True, f"ERROR: number value cannot be empty"),
            TestCase("  ", False, 0, True, f"ERROR: number value cannot be empty"),
        ]

        for testcase in testcases:
            self.assertEqual(testcase.output, self.constraintPair.set_uppercase_count(testcase.input))
            if testcase.is_error:
                self.assertEqual(testcase.error, self.constraintPair.get_error_msg())
            else:
                self.assertEqual(testcase.actual_value, self.constraintPair.min_uppercase_count)

    def test_set_symbol_count(self):
        class TestCase:
            def __init__(self, input: str, output: bool, actual_value: int, is_error: bool, error: str):
                self.input: str = input 
                self.output: bool = output
                self.actual_value: int = actual_value
                self.is_error: bool = is_error
                self.error: str = error

        testcases: List[TestCase] = [
            TestCase("1", True, 1, False, ""),
            TestCase("2", True, 2, False, ""),
            TestCase("3", True, 3, False, ""),
            TestCase("30000", True, 30000, False, ""),
            TestCase("-1", False, 0, True, f"ERROR: symbol character count cannot be negative: -1"),
            TestCase("-234", False, 0, True, f"ERROR: symbol character count cannot be negative: -234"),
            TestCase("-234.23423", False, 0, True, f"ERROR: symbol character count cannot be negative: -234"),
            TestCase("234wrong_text", False, 0, True, f"ERROR: invalid integer value: 234wrong_text"),
            TestCase("wwwww234242fsdf!@#$!$#!", False, 0, True, f"ERROR: invalid integer value: wwwww234242fsdf!@#$!$#!"),
            TestCase("", False, 0, True, f"ERROR: number value cannot be empty"),
            TestCase("  ", False, 0, True, f"ERROR: number value cannot be empty"),
        ]

        for testcase in testcases:
            self.assertEqual(testcase.output, self.constraintPair.set_symbol_count(testcase.input))
            if testcase.is_error:
                self.assertEqual(testcase.error, self.constraintPair.get_error_msg())
            else:
                self.assertEqual(testcase.actual_value, self.constraintPair.min_symbol_count)