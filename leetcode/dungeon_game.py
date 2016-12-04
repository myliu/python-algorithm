class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = max(1, 1-dungeon[i][j])
                elif i == m-1:
                    dp[i][j] = max(1, dp[i][j+1]-dungeon[i][j])
                elif j == n-1:
                    dp[i][j] = max(1, dp[i+1][j]-dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i][j+1]-dungeon[i][j], dp[i+1][j]-dungeon[i][j]))
        return dp[0][0]