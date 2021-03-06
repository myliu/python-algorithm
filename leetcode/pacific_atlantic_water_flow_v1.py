from collections import deque

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        pq = deque()
        aq = deque()
        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            pq += (i, 0),
            aq += (i, n-1),
            pacific[i][0] = True
            atlantic[i][n-1] = True

        for i in range(n):
            pq += (0, i),
            aq += (m-1, i),
            pacific[0][i] = True
            atlantic[m-1][i] = True

        self.bfs(matrix, pq, pacific)
        self.bfs(matrix, aq, atlantic)

        results = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    results += [i, j],
        return results

    def bfs(self, matrix, queue, visited):
        m, n = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y] and matrix[x][y] >= matrix[i][j]:
                    visited[x][y] = True
                    queue += (x, y),