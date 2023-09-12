class Solution(object):
    def climbStairs(self, n):
        """
        ****
        Problem: You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        ****

        Restatement of the problem:
        1. Figure out how many sequences created from the set {1, 2} can sum to an integer N.
        Examples:
        - N=1 -> 1
        - N=2 -> (1,1), (2)
        - N=3 -> (1, 1, 1), (1, 2), (2, 1)
        - N=4 -> (1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 2)

        The insight here is that the number of ways to get to N is the same as the number of ways to get to N-1, just
        with a 1 appended on the end of each sequence. Similarly with N-2 and appending a 2 on the end of each
        sequence. So, something like:

            climbStairs(N) = climbStairs(N-1) + climbStairs(N-2)

        Naively we could repeatedly iterate over the 1, 2 and bulid up larger and larger
        sequences and check their sums, but that is very inefficient. And actually may be harder to code correctly than
        what I'm thinking.

        Instead we could just initialize an array of length N, with the values of 0, 1 and 2 already known. Then we get
        the value of the next index by summing the values of the two previous indices and so on until we are done. Then
        the value of the last index will be our answer.

        Analysis: Both space and time complexity are linear with the size of N.

        Edge cases:
         - 0
         - empty

        :type n: int
        :rtype: int
        """
        if n in [0, 1, 2]:
            return n

        # Let's create an index for 0 so we can have the nice effect of the index corresponding to the value of N
        ways = [0] * (n + 1)
        ways[0], ways[1], ways[2] = 0, 1, 2

        for i in range(3, len(ways)):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[-1]
