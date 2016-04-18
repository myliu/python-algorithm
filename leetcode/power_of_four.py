class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 0 and num & 3 == 0:
            num >>= 2
        return num == 1