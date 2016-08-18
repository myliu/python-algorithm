class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(nums, i, tmp, res, k):
            if len(tmp) == k:
                res.append(list(tmp))
                return

            while i < len(nums):
                dfs(nums, i+1, tmp+(nums[i],), res, k)
                i += 1

        nums = range(1, n+1)    
        res = []
        dfs(nums, 0, (), res, k)
        return res