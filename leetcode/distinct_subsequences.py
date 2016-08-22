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
        dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

        for i in range(len(s)+1):
            dp[i][0] = 1

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(s)][len(t)]