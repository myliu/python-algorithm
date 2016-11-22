class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)

        if k > n/2:
            return self.quick_solution(prices)

        dp = [[0 for _ in range(n)] for _ in range(k+1)]

        for i in range(1, k+1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j]+max_diff)
                max_diff = max(max_diff, dp[i-1][j]-prices[j])
        return dp[k][n-1]

    def quick_solution(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit