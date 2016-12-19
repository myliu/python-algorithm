class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row, col = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row += i,
                    col += j,
        return self.min_dist(sorted(row)) + self.min_dist(sorted(col))

    def min_dist(self, people):
        i, j, dist = 0, len(people)-1, 0
        while i < j:
            dist += people[j] - people[i]
            i += 1
            j -= 1
        return dist