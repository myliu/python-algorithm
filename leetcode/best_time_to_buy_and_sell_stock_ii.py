class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        _max = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            _max += diff if diff > 0 else 0
        return _max