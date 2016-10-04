class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = range(1, n+1)
        while len(nums) > 1:
            nums = nums[1::2][::-1]
        return nums[0]