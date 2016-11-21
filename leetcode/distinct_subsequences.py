class Solution(object):

    """
        ''  r   a   b   b   i   t   --> t
    ''  1   0   0   0   0   0   0
    r   1   1   0   0   0   0   0
    a   1   1   1   0   0   0   0
    b   1   1   1   1   0   0   0
    b   1   1   1   2   1   0   0
    b   1   1   1   3   3   0   0
    i   1   1   1   3   3   3   0
    t   1   1   1   3   3   3   3

    \|/
    s
    """
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

        for i in range(len(s)+1):
            dp[i][0] = 1

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]

        return dp[len(s)][len(t)]