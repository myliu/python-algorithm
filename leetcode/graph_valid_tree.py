class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False

        parents = range(n)

        def find(k):
            return k if k == parents[k] else find(parents[k])

        def union(xy):
            x, y = map(find, xy)
            parents[x] = y
            return x != y

        return all(map(union, edges))