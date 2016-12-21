from collections import defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        adj = defaultdict(set)
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in adj if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    new_leaves += j,
            leaves = new_leaves

        return leaves