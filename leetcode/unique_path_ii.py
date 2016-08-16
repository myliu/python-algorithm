class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(obstacleGrid[0])
        dp[0] = 1
        for row in obstacleGrid:
            for i, c in enumerate(row):
                if c == 1:
                    dp[i] = 0
                elif i > 0:
                    dp[i] += dp[i-1]
        return dp[-1]