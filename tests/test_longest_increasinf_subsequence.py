from dynamic_programming.longest_increasing_subsequence import Solution

from .utilities import TestCase


def test_length_of_LIS() -> None:
    length_of_LIS = Solution().lengthOfLIS

    cases = [
        TestCase(input=[10, 9, 2, 5, 3, 7, 101, 18], want=4),
        TestCase(input=[0, 1, 0, 3, 2, 3], want=4),
        TestCase(input=[7, 7, 7, 7, 7, 7, 7], want=1),
    ]

    for case in cases:
        assert length_of_LIS(case.input) == case.want
