class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s == '0':
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        dp[n-1] = 1 if s[n-1] != '0' else 0

        for i in range(n-2, -1, -1):
            if s[i] == '0':
                continue
            dp[i] = dp[i+1] + dp[i+2] if int(s[i:i+2]) <= 26 else dp[i+1]

        return dp[0]