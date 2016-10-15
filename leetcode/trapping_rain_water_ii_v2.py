import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        m, n = len(heightMap), len(heightMap[0])

        heap = []
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(n):
            heapq.heappush(heap, (heightMap[0][i], 0, i))
            visited[0][i] = True
            heapq.heappush(heap, (heightMap[m-1][i], m-1, i))
            visited[m-1][i] = True

        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            visited[i][0] = True
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][n-1] = True

        result = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            height, i, j = heapq.heappop(heap)
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y]:
                    if heightMap[x][y] < height:
                        result += height - heightMap[x][y]
                    visited[x][y] = True
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
        return result