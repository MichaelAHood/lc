class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Problem restatement:
            find a subsequence, defined by indices increase from left to right, where the values
            are strictly increasing, i.e. each value is greater than the value before.

        Examples:
            nums = [10,9,2,5,3,7,101,18] -> 4
            nums = [0,1,0,3,2,3] -> 4
            nums = [7,7,7,7,7,7,7] -> 1

        Discussion:
           Initialize an array of 1's the size of our array of numbers to store the size of the largest
           subsequence up to that index.

           We will iterate through the numbers array and define a lookback window that will iterate
           backwards through all of the numbers before the current index. At each of those
           previous numbers if the current number is bigger than the previous we take the max of
           the current longth at that index or the length of the previous index + 1. If this new value
           is greater than the max_length so far, we update it and break out of the iteration.

        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        lengths = [1] * N
        max_length = 1

        for i in range(1, N):
            # begin lookback
            for j in reversed(range(i)):
                if nums[i] > nums[j]:
                    lengths[i] = max(lengths[i], 1 + lengths[j])
                if lengths[i] > max_length:
                    # stop lookback condition
                    max_length = lengths[i]
                    break
        return max_length
