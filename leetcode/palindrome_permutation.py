class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        for c in s:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1

        odd_value_num = 0
        for v in d.itervalues():
            if v % 2 == 1:
                odd_value_num += 1
        return False if odd_value_num > 1 else True