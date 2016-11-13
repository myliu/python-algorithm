class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(range(1, n+1), k, 0, (), result)
        return result
    
    def dfs(self, nums, k, i, tmp, result):
        if len(tmp) == k:
            result += list(tmp),
            return
        
        while i < len(nums):
            self.dfs(nums, k, i+1, tmp+(nums[i],), result)
            i += 1