class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) - p.count('*') > len(s):
            return False

        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True

        for j in xrange(len(p)):
            dp[0][j+1] = dp[0][j] and p[j] == '*'

        for j in xrange(len(p)):
            for i in xrange(len(s)):
                if p[j] != '*':
                    dp[i+1][j+1] = dp[i][j] and (p[j] == s[i] or p[j] == '?')
                else:
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]

        return dp[len(s)][len(p)]