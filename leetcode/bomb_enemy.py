class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        res = 0
        col_hits = [0] * n
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if j == 0 or row[j-1] == 'W':
                    row_hits = 0
                    k = j
                    while k < n and row[k] != 'W':
                        if row[k] == 'E':
                            row_hits += 1
                        k += 1
                if i == 0 or grid[i-1][j] == 'W':
                    col_hits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_hits[j] += 1
                        k += 1
                if cell == '0':
                    res = max(res, row_hits + col_hits[j])
        return res