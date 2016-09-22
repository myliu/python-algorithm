class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, m, n, cache):
            if cache[i][j]:
                return cache[i][j]

            max_len = 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                    continue
                max_len = max(max_len, 1 + dfs(x, y, m, n, cache))
            cache[i][j] = max_len
            return max_len

        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        cache =[[0 for _ in range(n)] for _ in range(m)]
        max_len = 1
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dfs(i, j, m, n, cache))
        return max_len