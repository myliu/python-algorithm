from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        m, n = len(rooms), len(rooms[0])
        gates = []
        for i in range(m):
            for j in range(n):
                if not rooms[i][j]:
                    gates += (i, j, 0),

        for gate in gates:
            queue = deque()
            queue += gate,
            visited = set()
            while queue:
                i, j, dist = queue.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] not in (-1, 0) and (x, y) not in visited:
                        rooms[x][y] = min(rooms[x][y], dist+1)
                        visited.add((x, y))
                        queue += (x, y, dist+1),