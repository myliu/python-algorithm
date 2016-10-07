from collections import defaultdict
from itertools import permutations

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = defaultdict(dict)
        for (start, end), val in zip(equations, values):
            d[start][end] = val
            d[start][start] = 1.0
            d[end][end] = 1.0
            d[end][start] = 1/val
        for i, j, k in permutations(d, 3):
            if j in d[i] and k in d[j]:
                d[i][k] = d[i][j] * d[j][k]
        return [d[i].get(j, -1.0) for i, j in queries]