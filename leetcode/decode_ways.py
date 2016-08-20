class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s == '0':
            return 0

        n = len(s)
        res = [0] * (n+1)
        res[n] = 1
        res[n-1] = 1 if s[n-1] != '0' else 0
        for i in range(n-2, -1, -1):
            if s[i] == '0':
                continue
            res[i] = res[i+1]+res[i+2] if int(s[i:i+2]) <= 26 else res[i+1]
        return res[0]