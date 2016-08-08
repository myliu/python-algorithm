class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            i, temp = 1, divisor
            while dividend >= temp:
                dividend -= temp
                res += i
                temp <<= 1
                i <<= 1

        if positive:
            return min(2**31-1, res)
        else:
            return max(-2**31, -res)