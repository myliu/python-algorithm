"""
Reference: https://discuss.leetcode.com/topic/12133/bit-operation-solution-java/22
12: 1100
15: 1111

We don't have to worry about the numbers between 12 and 15.
At each step, we right-shift both numbers if they are different.
Eventually, m == n == 11 when i = 2.
Then we shift either m or n to the left by i == 2, we get 1100.
"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i