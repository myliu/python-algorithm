class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        results = []
        prev = nums[0]
        nums.append(-1)
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if nums[i-1] == prev:
                    results.append(str(prev))
                else:
                    results.append(str(prev) + '->' + str(nums[i-1]))
                prev = nums[i]
        return results