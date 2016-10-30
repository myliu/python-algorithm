class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        end = 0
        for num in nums:
            if num != val:
                nums[end] = num
                end += 1
        return end