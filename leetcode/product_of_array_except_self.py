class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n

        # left to right scan
        prev = 1
        for i in range(1, n):
            prev *= nums[i-1]
            result[i] *= prev

        # right to left scan
        prev = 1
        for i in range(n-2, -1, -1):
            prev *= nums[i+1]
            result[i] *= prev

        return result