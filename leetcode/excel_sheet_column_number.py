import math

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        m = 0
        for i in range(len(s)):
            m += self.charToInt(s[len(s)-1-i]) * int(math.pow(26, i))
        return m

    def charToInt(self, c):
        return ord(c) - ord('A') + 1

if __name__ == '__main__':
    s = Solution()
    print s.titleToNumber('AC')