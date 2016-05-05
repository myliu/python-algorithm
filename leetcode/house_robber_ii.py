class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        i, e = 0, 0
        for num in nums:
            i, e = e + num, max(i, e)
        return max(i, e)