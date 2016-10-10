from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        odd = False
        even = 0
        for k, v in counter.iteritems():
            if v % 2 == 0:
                even += v
            else:
                even += v - 1
                odd = True
        return even + (1 if odd else 0)