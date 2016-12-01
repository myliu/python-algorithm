class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.insert(0, lower-1)
        nums.append(upper+1)

        results = []
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                results.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                results.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))
        return results