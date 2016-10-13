class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j, carry, result = 0, 0, 0, []
        while i < len(num1) or j < len(num2) or carry:
            if i < len(num1):
                carry += ord(num1[::-1][i]) - ord('0')
                i += 1
            if j < len(num2):
                carry += ord(num2[::-1][j]) - ord('0')
                j += 1
            result += carry % 10,
            carry /= 10
        return ''.join([chr(c + ord('0')) for c in result[::-1]])