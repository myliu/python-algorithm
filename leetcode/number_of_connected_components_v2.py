class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        nodes = range(n)

        # Find the leader of k
        # 1) Update nodes with leader
        # 2) Return leader
        def find(k):
            if k != nodes[k]:
                nodes[k] = find(nodes[k])
            return nodes[k]

        # Point the leader of i to the leader of j
        def union(i, j):
            nodes[find(i)] = find(j)

        for i, j in edges:
            union(i, j)

        # Count the number of leaders
        return len(set(map(find, nodes)))