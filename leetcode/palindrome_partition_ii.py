class Solution(object):

    # https://discuss.leetcode.com/topic/2840/my-solution-does-not-need-a-table-for-palindrome-is-it-right-it-uses-only-o-n-space
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
            while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
                cuts[i+j+1] = min(cuts[i+j+1], cuts[i-j]+1)
                j += 1

            # Even length palindrome
            j = 1
            while i - j + 1 >= 0 and i + j < n and s[i-j+1] == s[i+j]:
                cuts[i+j+1] = min(cuts[i+j+1], cuts[i-j+1]+1)
                j += 1

        return cuts[n]