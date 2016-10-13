class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)

        if total % 2 == 1:
            return False

        half = total / 2
        dp = [False for _ in range(half+1)]
        dp[0] = True
        for num in nums:
            for i in range(half, 0, -1):
                if i >= num:
                    dp[i] = dp[i] or dp[i-num]
        return dp[half]