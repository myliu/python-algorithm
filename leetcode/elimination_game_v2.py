class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, count, step = 1, n, 1
        while count > 1:
            end = start + (count - 1) * step
            start = end - (count % 2) * step
            count /= 2
            step *= -2
        return start