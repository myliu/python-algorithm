import math  

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(n, start, upper, tmp, result):
            if n == 1 and len(tmp) > 1:
                result += tmp,
                return

            i = start
            while i <= n:
                if i > upper:
                    i = n
                if n % i == 0:
                    dfs(n/i, i, math.sqrt(n/i), tmp+[i], result)
                i += 1

        result = []
        dfs(n, 2, math.sqrt(n), [], result)
        return result