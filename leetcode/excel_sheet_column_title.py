class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        while n > 0:
            n -= 1
            s = chr(ord('A') + n%26) + s
            n /= 26
        return s