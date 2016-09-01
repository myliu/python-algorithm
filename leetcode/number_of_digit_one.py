class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones, m = 0, 1
        while m <= n:
            # Case 1: The mth position is 2->9
            ones += (n/m+8)/10 * m
            # Case 2: The mth position is 1
            if n/m % 10 == 1:
                ones += n%m + 1
            # Case 3: The mth position is 0 (no-op)

            m *= 10
        return ones