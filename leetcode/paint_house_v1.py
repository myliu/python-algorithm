class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or len(costs) == 0:
            return 0
            
        if len(costs) == 1:
            return min(costs[0])

        dp = [[0 for j in range(len(costs[i]))] for i in range(len(costs))]
        dp[0] = costs[0]
        
        for i in xrange(1, len(costs)):
            for j in xrange(len(costs[i])):
                if j == 0:
                    dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
                elif j == 1:
                    dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
                else:
                    dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        return min(dp[len(costs)-1])