class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = running_max = nums[0]
        for i in range(1, len(nums)):
            running_max = max(running_max + nums[i], nums[i])
            _max = max(_max, running_max)
        return _max