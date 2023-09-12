from dynamic_programming.longest_common_subsequence import Solution

from .utilities import TestCase


def test_length_of_LCS() -> None:
    length_of_LCS = Solution().lengthLCS

    cases = [
        TestCase(input=("abcde", "ace"), want=3),
        TestCase(input=("abc", "abc"), want=3),
        TestCase(input=("abc", "def"), want=0),
        TestCase(input=("cdeaq", "zcdgaecdxlea"), want=4),
    ]

    for case in cases:
        assert length_of_LCS(*case.input) == case.want
