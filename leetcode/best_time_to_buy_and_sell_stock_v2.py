class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        curr_min = prices[0]
        profit = 0
        for price in prices[1:]:
            profit = max(profit, price - curr_min)
            curr_min = min(curr_min, price)
        return profit