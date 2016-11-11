class Solution(object):
    # http://www.matrix67.com/blog/archives/361
    def mySqrt(self, a):
        """
        :type a: int
        :rtype: int
        """
        # Randomly pick the square root of a to be a
        x = a
        # Use Newton's method to continuously find better x
        # f(x) = x^2 - a
        # 2x is the derivative of f(x)
        # x' = x - f(x)/2x = x - (x^2-a)/2x = x - x/2 + a/2x = (x + a/x) / 2
        while x * x > a:
            x = (x + a/x) / 2
        return x