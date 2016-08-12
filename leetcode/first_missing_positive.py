class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        for i in xrange(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                swap(nums, i, nums[i]-1)

        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1
        
        return len(nums) + 1