class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        dp[0] = 1
        for t in range(1, target+1):
            for num in nums:
                if t >= num:
                    dp[t] += dp[t-num]
        return dp[target]