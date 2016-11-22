class Solution(object):

    # Kadane's algorithm
    # https://discuss.leetcode.com/topic/19853/kadane-s-algorithm-since-no-one-has-mentioned-about-this-so-far-in-case-if-interviewer-twists-the-input
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        _max = running_max = 0
        for i in range(1, len(prices)):
            running_max = max(0, running_max+prices[i]-prices[i-1])
            _max = max(_max, running_max)
        return _max