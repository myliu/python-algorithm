class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [0] * (n+1)
        cache[0] = cache[1] = 1
        for i in xrange(2, n+1):
            for j in xrange(1, i+1):
                cache[i] += cache[j-1] * cache[i-j]
        return cache[n]