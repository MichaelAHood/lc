from dynamic_programming.climb_stairs import Solution

from .utilities import TestCase


def test_climbing_stairs() -> None:
    climb_stairs = Solution().climbStairs

    cases = [
        TestCase(input=0, want=0),
        TestCase(input=1, want=1),
        TestCase(input=2, want=2),
        TestCase(input=3, want=3),
        TestCase(input=4, want=5),
        TestCase(input=5, want=8),
        TestCase(input=6, want=13),
    ]

    for case in cases:
        assert climb_stairs(case.input) == case.want
