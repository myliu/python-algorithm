from collections import deque

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        buildings = [[0 for _ in range(n)] for _ in range(m)]
        distances = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        building_count = 0

        for i in range(m):
            for j in range(n):
                # For each building, do BFS
                if grid[i][j] == 1:
                    building_count += 1

                    # queue: (distance, x, y)
                    queue = deque()
                    queue += (0, i, j),
                    visited = [[False for _ in range(n)] for _ in range(m)]
                    visited[i][j] = True
                    while queue:
                        distance, row, column = queue.popleft()
                        for dx, dy in directions:
                            x, y = row + dx, column + dy
                            if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y] and grid[x][y] == 0:
                                buildings[x][y] += 1
                                distances[x][y] += distance + 1
                                visited[x][y] = True
                                queue += (distance+1, x, y),

        shortest_distance = float('inf')
        for i in range(m):
            for j in range(n):
                if buildings[i][j] == building_count:
                    shortest_distance = min(shortest_distance, distances[i][j])
        return shortest_distance if shortest_distance != float('inf') else -1