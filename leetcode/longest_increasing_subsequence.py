class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        lis = [1] * len(nums)
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    lis[j] = max(lis[j], lis[i] + 1)

        return max(lis)