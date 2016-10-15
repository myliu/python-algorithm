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
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while heap:
            height, x, y = heapq.heappop(heap)
            for i, j in directions:
                xx, yy = x+i, y+j
                if xx >= 0 and xx <= m-1 and yy >= 0 and yy <= n-1 and not visited[xx][yy]:
                    visited[xx][yy] = True
                    result += max(0, height-heightMap[xx][yy])
                    heapq.heappush(heap, (max(height, heightMap[xx][yy]), xx, yy))
        return result