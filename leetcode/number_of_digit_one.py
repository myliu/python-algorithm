class Solution(object):

    # https://discuss.leetcode.com/topic/18054/4-lines-o-log-n-c-java-python
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones, i = 0, 1
        while i <= n:
            # Case 1: The ith position is 2->9
            ones += (n/i+8)/10 * i
            # Case 2: The ith position is 1
            if n/i % 10 == 1:
                ones += n%i + 1
            # Case 3: The ith position is 0 (no-op)

            i *= 10
        return ones