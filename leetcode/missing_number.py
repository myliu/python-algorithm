class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = max(nums)
        s = sum(nums)
        t = sum(range(largest + 1)) if largest == len(nums) else sum(range(largest + 2))
        return t - s