class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(abs(x))
        num = 0
        for i in xrange(len(s)-1, -1, -1):
            num = num * 10 + int(s[i])

        # Python actually can handle long int,
        # it is sad that OJ thinks all languages cannot handle integer longer than 32-bit
        # In order to pass the OJ, we would need to hard-code the largest int 0x7FFFFFFF
        if x >= 0:
            return num if num < 0x7FFFFFFF else 0
        else:
            return -num if num < 0x7FFFFFFF else 0