import collections

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2)
        if c1 != c2:
            return False

        n = len(s1)
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[(n-i):]) and self.isScramble(s1[i:], s2[:(n-i)]):
                return True
        return False