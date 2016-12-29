class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, m, n, cache):
            if cache[i][j]:
                return cache[i][j]

            _max = 1
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    _max = max(_max, dfs(x, y, m, n, cache) + 1)
            cache[i][j] = _max
            return _max

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        _max = 0
        cache = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                _max = max(_max, dfs(i, j, m, n, cache))
        return _max