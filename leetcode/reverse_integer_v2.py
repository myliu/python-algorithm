class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = int(str(abs(x))[::-1])

        if x >= 0:
            return num if num <= 2**31 - 1 else 0
        else:
            return -num if -num >= -2**31 else 0