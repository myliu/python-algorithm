class Solution(object):

    # A valid tree has two properties:
    # 1) No Cycles: number of edges equals to number of nodes minus 1
    # 2) Connected
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False

        nodes = range(n)

        def find(k):
            if k != nodes[k]:
                nodes[k] = find(nodes[k])
            return nodes[k]

        def union(i, j):
            nodes[find(i)] = find(j)

        for i, j in edges:
            union(i, j)

        return len(set(map(find, nodes))) == 1