class Solution(object):

    """
        ''  a   *   -> j(p)
    ''  T   F   T
    a   F   T   T
    a   F   F   T
    a   F   F   T
    a   F   F   T
    
    i(s)
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]

        dp[0][0] = True
        
        for k, v in enumerate(p):
            if v == '*' and dp[0][k-1]:
                dp[0][k+1] = True

        for i in xrange(len(s)):
            for j in xrange(len(p)):
                if p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j-1] != s[i] and p[j-1] != '.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j] or dp[i][j+1]

        return dp[len(s)][len(p)]