class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n:
            n -= 1
            remainder = n % 26
            result = chr(ord('A') + remainder) + result
            n /= 26
        return result