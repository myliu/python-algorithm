class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t = iter(t)
        for c in s:
            if c not in t:
                return False
        return True