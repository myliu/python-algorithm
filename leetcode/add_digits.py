class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num / 10 < 1:
            return num

        next = 0
        while num:
            next += num % 10
            num /= 10

        return self.addDigits(next)