class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = [lower-1] + nums + [upper+1]
        n = len(nums)
        result = []
        for i in range(n-1):
            if nums[i+1] - nums[i] == 2:
                result += str(nums[i]+1),
            elif nums[i+1] - nums[i] > 2:
                result += str(nums[i]+1) + '->' + str(nums[i+1]-1),
        return result