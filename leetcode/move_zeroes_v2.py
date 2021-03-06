class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        end = 0
        for num in nums:
            if num:
                nums[end] = num
                end += 1

        for i in range(end, len(nums)):
            nums[i] = 0