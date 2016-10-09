class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        len = 1
        count = 9
        start = 1

        while n > len * count:
            n -= len * count
            len += 1
            count *= 10
            start *= 10

        num = start + (n-1)/len
        return int(str(num)[(n-1)%len])