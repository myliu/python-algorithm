class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
        for i, v in enumerate(s):
            d1[ord(v)].append(i)
        for i, v in enumerate(t):
            d2[ord(v)].append(i)
        return sorted(d1) == sorted(d2)