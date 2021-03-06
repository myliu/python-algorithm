class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator:
            return '0'

        fraction = ''
        if (numerator > 0) != (denominator > 0):
            fraction += '-'

        numerator = abs(numerator)
        denominator = abs(denominator)
        fraction += str(numerator / denominator)
        remainder = numerator % denominator

        if not remainder:
            return fraction

        fraction += '.'

        d = {}
        while remainder:
            if remainder in d:
                i = d[remainder]
                return fraction[:i] + '(' + fraction[i:] + ')'
 
            d[remainder] = len(fraction)
            remainder *= 10
            fraction += str(remainder / denominator)
            remainder %= denominator
        return fraction