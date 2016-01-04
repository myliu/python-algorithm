class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def is_valid(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                return True
            return False

        def find(node):
            i, j = node[0], node[1]
            if nodes[(i, j)] != (i, j):
                nodes[(i, j)] = find(nodes[(i, j)])
            return nodes[(i, j)]

        def union(node1, node2):
            nodes[find(node1)] = nodes[find(node2)]

        if not grid:
            return 0

        nodes = {}
        edges = []
        directions = [(0, 1), (1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # Initialize nodes where each node represents a disjoint set
                    nodes[(i, j)] = (i, j)
                    for m, n in directions:
                        x, y = i + m, j + n
                        if is_valid(x, y):
                            edges.append(((i, j), (x, y)))

        for node1, node2 in edges:
            union(node1, node2)

        return len(set(map(find, nodes.keys())))

if __name__ == '__main__':
    s = Solution()
    # grid = [['1','1','0','0','0'],
    #         ['1','1','0','0','0'],
    #         ['0','0','1','0','0'],
    #         ['0','0','0','1','1']]

    grid = ['1','1','0','1']
    print s.numIslands(grid)