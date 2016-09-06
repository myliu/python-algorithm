class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        # n == 2
        diff = k * (k-1)
        same = k
        i = 2
        while i < n:
            tmp = diff
            diff = same * (k-1) + diff * (k-1)
            same = tmp
            i += 1
        return diff + same