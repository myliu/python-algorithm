class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
            
        longest = ''
        for i in range(len(s)):
            longest = max(longest, helper(i, i), key=len)
            longest = max(longest, helper(i, i+1), key=len)
        return longest