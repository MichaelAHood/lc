from dynamic_programming.coin_change import Solution

from .utilities import TestCase


def test_coin_change() -> None:
    coin_change = Solution().coinChange

    cases = [
        TestCase(input=([1, 5], 0), want=0),
        TestCase(input=([1, 2, 5], 11), want=3),
        TestCase(input=([1], 1), want=1),
        TestCase(input=([3], 5), want=-1),
        TestCase(input=([1, 1001], 1000), want=1000),
    ]

    for case in cases:
        coins, amount = case.input
        assert coin_change(coins, amount) == case.want
