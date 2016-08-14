class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        for i in xrange(len(nums)-2, -1, -1):
            m = float('inf')
            for j in range(nums[i]):
                if i+j+1 > len(nums)-1:
                    break
                m = min(m, dp[i+j+1]+1)
            dp[i] = m
        return dp[0]