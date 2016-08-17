class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero, second = 0, len(nums)-1
        i = 0
        while i <= second:
            while nums[i] == 2 and i < second:
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1
            while nums[i] == 0 and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            i += 1