class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = len(s)
        while i > 0:
            if self.isPalindrome(s[:i]):
                return s[i:][::-1] + s
            i -= 1
        return ""

    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome('aacecaa')
    print s.shortestPalindrome('aacecaaa')