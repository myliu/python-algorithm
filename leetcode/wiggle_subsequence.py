class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return 1

        k = 1
        while k < n and nums[k] == nums[k-1]:
            k += 1
        if k == n:
            return 1

        count = 1
        big = True if nums[k] > nums[k-1] else False
        for i in range(k, n):
            if (big and nums[i] > nums[i-1]) or (not big and nums[i] < nums[i-1]):
                count += 1
                big = not big
        return count