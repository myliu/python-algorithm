class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(sorted(nums), 0, (), result)
        return result

    def dfs(self, nums, start, tmp, result):
        result += tmp,
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, tmp+(nums[i],), result)