# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # l: lower bound
        # r: upper bound
        # x: current number
        l, r, x = 0, n, n/2
        while True:
            result = guess(x)
            if result == 0:
                return x
            elif result == 1:
                l = x
                # We have x + 1 here because in the case of (r-x)/2==0, we need to make sure x is move right by at least 1
                x = x + 1 + (r-x)/2
            else:
                r = x
                x = l + (x-l)/2