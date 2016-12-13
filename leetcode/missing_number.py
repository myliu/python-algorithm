class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = max(nums)
        actual = sum(nums)
        expected = sum(range(_max+1)) if _max == len(nums) else sum(range(_max+2))
        return expected - actual