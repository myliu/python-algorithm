from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        def valid_point(i, j, visited):
            if (i, j) in visited:
                return False
            if 0 <= i < len(rooms) and 0 <= j < len(rooms[0]) and rooms[i][j] != 0 and rooms[i][j] != -1:
                   return True
            return False
            
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    visited = set()
                    visited.add((i, j))
                    q = deque()
                    q.append((i, j, 0))
                    while q:
                        x, y, dist = q.popleft()
                        for m, n in directions:
                            x_next = x + m
                            y_next = y + n
                            if valid_point(x_next, y_next, visited):
                                visited.add((x_next, y_next))
                                q.append((x_next, y_next, dist+1))
                                rooms[x_next][y_next] = min(rooms[x_next][y_next], dist+1)