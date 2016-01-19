class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or len(costs) == 0:
            return 0

        if len(costs) == 1:
            return min(costs[0])

        k = len(costs[0])
        prev = [0] * k
        for now in costs:
            prev = [now[i] + min(prev[:i] + prev[i+1:]) for i in range(k)]
        return min(prev)