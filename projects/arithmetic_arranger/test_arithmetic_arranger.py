import unittest
from typing import List, Tuple
from main import arithmetic_arranger

class TestArranger(unittest.TestCase):
    def test_arithmetic_arranger(self):
        testcases: List[Tuple[List[str], bool, str]] = [
            (
                ["3801 - 2", "123 + 49"],
                False,
                "  3801      123\n-    2    +  49\n------    -----",
            ),
            (
                ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"],
                False,
                "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----",
            ),
            (
                ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"],
                False,
                "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------",
            ),
            (
                ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"],
                False,
                "Error: Too many problems.",
            ),
            (
                ["3 / 855", "3801 - 2", "45 + 43", "123 + 49"],
                False,
                "Error: Operator must be '+' or '-'.",
            ),
            (
                ["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"],
                False,
                "Error: Numbers cannot be more than four digits.",
            ),
            (
                ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"],
                False,
                "Error: Numbers must only contain digits.",
            ),
            (
                ["3 + 855", "988 + 40"],
                True,
                "    3      988\n+ 855    +  40\n-----    -----\n  858     1028",
            ),
            (
                ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"],
                True,
                "   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028",
            ),
        ]

        for testcase in testcases:
            self.assertEqual(arithmetic_arranger(problems=testcase[0], show_answers=testcase[1]), testcase[2])

if __name__ == '__main__':
    unittest.main()