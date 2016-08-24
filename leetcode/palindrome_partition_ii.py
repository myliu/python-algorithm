class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cuts = [i-1 for i in range(n+1)]
        for i in range(n):
            # Odd length palindrome
            j = 0
            while i-j >= 0 and i+j <= n-1 and s[i+j] == s[i-j]:
                cuts[i+j+1] = min(cuts[i+j+1], cuts[i-j]+1)
                j += 1

            # Even length palindrome
            j = 1
            while i-j+1 >= 0 and i+j <= n-1 and s[i+j] == s[i-j+1]:
                cuts[i+j+1] = min(cuts[i+j+1], cuts[i-j+1]+1)
                j += 1
        return cuts[n]