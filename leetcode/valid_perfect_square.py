class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Newton's Method
        # http://www.matrix67.com/blog/archives/361
        # https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=x%5E2-4%20graph
        x = num
        while x * x > num:
            # x = x - f(x)/2x
            # x = x - (x^2 - num) / 2x
            x = (x + num/x) / 2
        return x * x == num