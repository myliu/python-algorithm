class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True