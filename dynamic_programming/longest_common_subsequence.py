class Solution(object):
    def lengthLCS(self, text1: str, text2: str):
        """
        Problem: Find the the length of the longest common subsequence between two strings.

        Discussion: This smells like a dynamic programming problem. Maximizing some property
        of two indexible objects and the fact that it involes sequences lends itself to
        iteratively bulding up values in a grid.

        Plan:
        We can start by constructing a m x n grid where m = len(input1)+1 and n = len(input2)+1.
        The plus 1 is to provide an extra row and column to intialize with zeros so we can
        keep track of when we don't have matching chars between the two input strings.

        For loop through the row index and the column index and check to see if the char at those
        input indices are equal.
        - If so, then we add 1 to the value at row-1 and col-1. This adds 1 to our longest running subsequence.
        - If not, then we carry forward the larger of the values at the prvious column or row.

        When the loop is done the bottom right cell will contain the maximum value.

        """

        m = len(text1) + 1
        n = len(text2) + 1

        # m x n -> m rows and n columns.
        D = [[0] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i - 1] == text2[j - 1]:
                    D[i][j] = 1 + D[i - 1][j - 1]
                else:
                    D[i][j] = max(
                        D[i][j - 1],
                        D[i - 1][j],
                    )
        return D[-1][-1]
