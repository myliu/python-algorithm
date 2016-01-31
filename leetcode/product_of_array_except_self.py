class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)

        # left to right scan
        prev = 1
        for i in xrange(1, len(nums)):
            prev = prev * nums[i-1]
            output[i] = prev

        # right to left scan
        prev = 1
        for i in xrange(len(nums)-2, -1, -1):
            prev = prev * nums[i+1]
            output[i] *= prev

        return output