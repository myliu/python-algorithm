class Solution(object):

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return any(s[i:i+2] == '++' and not self.canWin(s[:i] + '-' + s[i+2:])
            for i in xrange(len(s)))