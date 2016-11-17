class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n, k = len(s1), len(s2), len(s3)

        if m + n != k:
            return False

        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True

        for i in range(m):
            dp[i+1][0] = dp[i][0] and s1[i] == s3[i]

        for j in range(n):
            dp[0][j+1] = dp[0][j] and s2[j] == s3[j]

        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = (dp[i][j+1] and s1[i] == s3[i+j+1]) or (dp[i+1][j] and s2[j] == s3[i+j+1])

        return dp[m][n]

"""
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

[
    [True, False, False, False, False, False],
    [True, False, False, False, False, False],
    [True, True, True, True, True, False],
    [False, True, True, False, True, False],
    [False, False, True, True, True, True],
    [False, False, False, True, False, True]
]
"""