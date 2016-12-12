from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = Counter(s)
        odd = 0
        for i in counter.values():
            if i % 2 == 1:
                odd += 1
            if odd > 1:
                return False
        return True