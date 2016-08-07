class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[start] = nums[i]
                start += 1
        return start