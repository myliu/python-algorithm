class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        nodes = range(n)

        def find(k):
            # If k is not the root node
            if k != nodes[k]:
                # Let k points to the actual root of the set
                nodes[k] = find(nodes[k])
            return nodes[k]

        def union(m, n):
            # Let the root of m points to the root of n
            nodes[find(m)] = find(n)

        for m, n in edges:
            union(m, n)

        return len(set(map(find, nodes)))