class Solution(object):

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(s) == set(suffix):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicateLetters('cbacdcbc')