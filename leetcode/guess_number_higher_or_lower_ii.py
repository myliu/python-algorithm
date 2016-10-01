class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for len in range(1, n):
            i = 1
            j = i + len
            while j <= n:
                dp[i][j] = float('inf')
                for k in range(i, j+1):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
                i += 1
                j += 1
        return dp[1][n]