class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        prev = nums[0]
        nums += float('inf'),
        result = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if nums[i-1] == prev:
                    result += str(prev),
                else:
                    result += str(prev) + '->' + str(nums[i-1]),
                prev = nums[i]
        return result