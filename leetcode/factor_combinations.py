class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def factors(n, i, tmp, results):
            while i * i <= n:
                if n % i == 0:
                    results += tmp + [i, n/i],
                    factors(n/i, i, tmp+[i], results)
                i += 1
            return results
        return factors(n, 2, [], [])