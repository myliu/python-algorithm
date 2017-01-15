class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        while x > 0 or y > 0:
            count += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        return count