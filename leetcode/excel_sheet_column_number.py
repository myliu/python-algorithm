class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = 1
        result = 0
        for i in range(len(s)-1, -1, -1):
            result += k * (ord(s[i]) - ord('A') + 1)
            k *= 26
        return result

if __name__ == '__main__':
    s = Solution()
    print s.titleToNumber('AC')