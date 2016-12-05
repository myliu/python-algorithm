class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = [''] * 256, [''] * 256
        for i, v in enumerate(s):
            d1[ord(v)] += str(i)
        for i, v in enumerate(t):
            d2[ord(v)] += str(i)
        return set(d1) == set(d2)