class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x

        return self.myPow(x*x, n/2) if n % 2 == 0 else x * self.myPow(x*x, n/2)