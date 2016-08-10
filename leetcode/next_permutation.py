class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        # At this point, nums[i-1] is the number to number to be swapped

        if i != 0:
            j = len(nums) - 1
            while j > i - 1:
                if nums[j] > nums[i-1]:
                    tmp = nums[j]
                    nums[j] = nums[i-1]
                    nums[i-1] = tmp
                    break
                j -= 1

        nums[i:] = nums[i:][::-1]