class Solution(object):
    def coinChange(self, coins, amount):
        """
        Problem with the greedy approach.
        coins = [2, 3], amount = 10 -> 7, 4, 1, -1 -> -1 Which is wrong.

        Initialize the array to minimize:
        ways = [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

        loop:
            # v indicates the start index of the iteration
                        v
            coin=1  0   1   2   3   4   5   6   7   8   9  10  11
            ways = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]

                            v
            coin=2  0   1   2   3   4   5   6   7   8   9  10  11
            ways = [0,  1,  1,  2,  2,  3,  3,  4,  4,  5,  5,  6]

                                        v
            coin=5  0   1   2   3   4   5   6   7   8   9  10  11
            ways = [0,  1,  1,  2,  2,  1,  2,  2,  3,  3,  2,  3]

        Discussion: Again the key insight here is that for any given coin denomination we use the fact that the number
        of ways to get any amount can be broken up into 1 + the number of ways to get amount - coin.

        Edge cases:
            - 0 should return 0


        A case that returns -1:
            coins = [3] amount = 5
        """
        # We can skip the work if amount is 0.
        if amount == 0:
            return 0

        # Initialize to a value that is impossible to obtain through a combination of the coins, i.e. even with
        # a coin=1 the total number of coins can only be up to amount, but not greater.
        # This serves as a starting point that can be minimized.
        ways = [amount + 1] * (amount + 1)

        # We need a way to indicate perfect change 0 in the case where amount - coin == 0.
        ways[0] = 0

        for coin in sorted(coins):
            for amount in range(coin, len(ways)):
                # With each successive coin we are checking how many are needed and choosing the smaller of the number
                # of the two.
                # The value for ways[amount] can only get smaller or stay the same.
                ways[amount] = min(ways[amount], 1 + ways[amount - coin])

        # -1 if we fail to minimize below the starting value of ways[amount].
        return -1 if ways[amount] == amount + 1 else ways[amount]
