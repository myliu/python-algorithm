from collections import deque

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = max(1, -dungeon[m-1][n-1] + 1)

        queue = deque()
        queue += (m-1, n-1),
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(0, -1), (-1, 0)]:
                i, j = x + dx, y + dy
                if self.is_valid(i, j):
                    dp[i][j] = max(1, min(dp[i][j], dp[x][y]-dungeon[i][j]))
                    queue += (i, j),
        return dp[0][0]

    def is_valid(self, i, j):
        if i >= 0 and j >= 0:
            return True
        return False