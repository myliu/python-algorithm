class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        
        if len(costs) == 1:
            return min(costs[0])
        
        n = len(costs[0])
        prev = [0] * n
        for cost in costs:
            prev = [cost[i]+min(prev[:i]+prev[i+1:]) for i in range(n)]
        return min(prev)