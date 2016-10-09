class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        d = '0123456789abcdef'
        result = ''
        for _ in range(8):
            idx = num & 15
            hex = d[idx]
            result = hex + result
            num >>= 4
        return result.lstrip('0')