class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(l, r, res):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            # Move this if statement outside the while loop simply for performance sake                
            if r - l - 1 > len(res):
                res = s[l+1:r]

            return res

        res = ''
        for i, v in enumerate(s):
            res = helper(i, i, res)
            res = helper(i, i+1, res)
        return res