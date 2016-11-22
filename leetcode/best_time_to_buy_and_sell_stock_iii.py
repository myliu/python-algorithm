class Solution(object):
    
    # https://www.youtube.com/watch?v=oDhu5uGq_ic
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        dp = [[0 for _ in range(n)] for _ in range(3)]
        
        # i is the number of transactions
        # j is the trading day
        for i in range(1, 3):
            # max_diff is the max profit with i-1 transactions on 0...j-1 day + the cost to buy stock on that day
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], max_diff+prices[j])
                max_diff = max(max_diff, dp[i-1][j]-prices[j])
        return dp[2][n-1]