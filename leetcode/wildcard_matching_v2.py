class Solution(object):

    """
        ''  a   *   -> j(p)
    ''  T   F   F
    a   F   T   T
    b   F   F   T
    c   F   F   T

    i(s)
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        if n - p.count('*') > m:
            return False

        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for i in range(n):
            dp[0][i+1] = dp[0][i] and p[i] == '*'

        for i in range(m):
            for j in range(n):
                if p[j] == '*':
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j] and p[j] in (s[i], '?')

        return dp[m][n]