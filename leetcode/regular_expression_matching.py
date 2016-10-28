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
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]

        dp[0][0] = True

        for i in range(n):
            if p[i] == '*':
                dp[0][i+1] = dp[0][i-1]

        for i in range(m):
            for j in range(n):
                if p[j] in (s[i], '.'):
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j-1] in (s[i], '.'):
                        dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j] or dp[i][j+1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j-1]

        return dp[m][n]