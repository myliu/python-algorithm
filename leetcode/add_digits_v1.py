class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num / 10 < 1:
            return num

        _next = 0
        while num:
            _next += num % 10
            num /= 10

        return self.addDigits(_next)