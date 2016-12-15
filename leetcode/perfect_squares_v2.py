class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0

        for i in range(1, n+1):
            _min = float('inf')
            j = 1
            while i - j * j >= 0:
                _min = min(_min, dp[i-j*j]+1)
                j += 1
            dp[i] = _min
        return dp[n]