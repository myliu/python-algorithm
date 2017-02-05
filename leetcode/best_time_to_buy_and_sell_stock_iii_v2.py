class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        right_max = [0] * n
        curr_max = prices[n-1]
        for i in range(n-1, -1, -1):
            curr_max = max(curr_max, prices[i])
            right_max[i] = curr_max

        curr_min = prices[0]
        first_profit = profit = 0
        for i in range(1, n):
            profit = max(profit, right_max[i] - prices[i] + first_profit)
            curr_min = min(curr_min, prices[i])
            first_profit = max(first_profit, prices[i] - curr_min)

        return max(profit, first_profit)