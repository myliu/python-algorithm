class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        length = len(s)
        dp = [True] + [False] * length

        if len(p) - p.count('*') > length:
            return False

        for i in p:
            if i != '*':
                for j in xrange(length, 0, -1):
                    dp[j] = dp[j-1] and (i == s[j-1] or i == '?')
            else:
                for j in xrange(1, length+1):
                    dp[j] = dp[j] or dp[j-1]
            dp[0] = dp[0] and i == '*'

        return dp[-1]