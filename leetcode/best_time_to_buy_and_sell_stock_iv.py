class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0

        n = len(prices)
        if k >= n/2:
            return self.quick_solution(prices)

        cache = [[0 for j in range(n)] for i in range(k+1)]
        for i in range(1, k+1):
            # At each level, buy stock on day 1
            # tmp_max is the max profit when we are holding a stock
            tmp_max = -prices[0]
            for j in range(1, n):
                # cache represents the max profit using i transaction on day j
                # If we do not close a transaction, max profit is the same as the previous day
                # Thus, cache[i][j] = cache[i][j-1]
                # If we do close a transaction, we can get prices[j] $ back
                # Remember, tmp_max presents the max profit when we are holding a stock
                cache[i][j] = max(cache[i][j-1], tmp_max+prices[j])
                # tmp_max is the real magic
                # If we continue holding the stock, tmp_max = tmp_max
                # If we sell the stock on the previous day, and buy new stock on day j
                # tmp_max = cache[i-1][j-1] - prices[j]
                tmp_max = max(tmp_max, cache[i-1][j-1]-prices[j])
        return cache[k][n-1]

    def quick_solution(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit