class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0

        b1 = -prices[0]
        s1 = s2 = 0
        for i in range(1, len(prices)):
            b0 = max(b1, s2-prices[i])
            s0 = max(s1, b1+prices[i])
            b1 = b0
            s2, s1 = s1, s0
        return s0