class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def factors(n, i, tmp, result):
            while i * i <= n:
                if n % i == 0:
                    result += tmp + [i, n/i],
                    factors(n/i, i, tmp+[i], result)
                i += 1
            return result
        return factors(n, 2, [], [])