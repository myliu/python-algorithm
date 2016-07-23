class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        base, count = 9, 10
        for i in xrange(2, n+1):
          base *= 10 - i + 1
          count += base
        return count