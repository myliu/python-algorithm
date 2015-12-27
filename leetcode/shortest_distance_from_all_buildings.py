from collections import deque

class Solution(object):

    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Test if (i, j) is a valid point
        # 1) if (i, j) has been visited before
        # 2) if (i, j) is a legitimate point
        def validate(i, j, visited):
            if (i, j) in visited:
                return -1
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                # Return 1 if grid[i][j] is a building
                if grid[i][j] == 1:
                    return 1
                # Return 0 is grid[i][j] is empty land
                elif grid[i][j] == 0:
                    return 0
            return -1

        # Determine the number of buildings on the grid
        num_buildings = sum(row.count(1) for row in grid)

        # first_trip and num_connected_buildings is used to optimize performance
        point_dict, first_trip, num_connected_buildings = {}, True, 1

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    visited = set()
                    visited.add((i, j))
                    q = deque()
                    q.append((i, j, 0))
                    while q:
                        x, y, dist = q.popleft()
                        for m, n in directions:
                            x_next = x + m
                            y_next = y + n
                            if first_trip and validate(x_next, y_next, visited) == 1:
                                visited.add((x_next,y_next))
                                num_connected_buildings = num_connected_buildings + 1
                                continue
                            if validate(x_next, y_next, visited) == 0:
                                visited.add((x_next,y_next))
                                q.append((x_next, y_next, dist+1))
                                if (x_next, y_next) not in point_dict:
                                    point_dict[(x_next, y_next)] = (1, dist+1)
                                else:
                                    point_dict[(x_next, y_next)] = (point_dict[(x_next, y_next)][0]+1, point_dict[(x_next, y_next)][1]+dist+1)
                    if first_trip and num_buildings != num_connected_buildings:
                        return -1
                    first_trip = False
        
        result = float('inf')
        for key in point_dict:
            if point_dict[key][0] == num_buildings:
                result = min(result, point_dict[key][1])
        return result if result != float('inf') else -1

if __name__ == '__main__':
    s = Solution()
    grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    print s.shortestDistance(grid)