class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def valid(i, j, grid):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                return True
            return False

        def find(node):
            if nodes[node] != node:
                nodes[node] = find(nodes[node])
            return nodes[node]
        
        def union(node1, node2):
            x, y = find(node1), find(node2)
            if x == y:
                return 0
            nodes[x] = y
            return 1

        grid = [[0 for j in range(n)] for i in range(m)]
        nodes = {}
        counts = []
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for pos in positions:
            count += 1
            i, j = pos[0], pos[1]
            grid[i][j] = 1
            nodes[(i, j)] = (i, j)
            for d in directions:
                x, y = i+d[0], j+d[1]
                if valid(x, y, grid):
                    count -= union((i, j), (x, y))
            counts.append(count)

        return counts

if __name__ == '__main__':
    s = Solution()
    print s.numIslands2(3, 3, [[0,0],[0,1],[1,2],[2,1]])
    # print s.numIslands2(2, 2, [[0,0],[1,1],[0,1]])