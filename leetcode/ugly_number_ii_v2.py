class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        p2 = p3 = p5 = 0
        for _ in range(1, n):
            _min = min((dp[p2]*2, dp[p3]*3, dp[p5]*5))
            if _min == dp[p2]*2:
                p2 += 1
            if _min == dp[p3]*3:
                p3 += 1
            if _min == dp[p5]*5:
                p5 += 1
            dp += _min,
        return dp[-1]