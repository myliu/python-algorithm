class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            i, tmp = 1, divisor
            while dividend >= tmp:
                dividend -= tmp
                result += i
                i <<= 1
                tmp <<= 1

        if positive:
            return min(2**31-1, result)
        else:
            return max(-2**31, -result)

if __name__ == '__main__':
    s = Solution()
    print s.divide(15, 3)