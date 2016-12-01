class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(n, start, tmp, result):
            if n <= 1:
                if len(tmp) > 1:
                    result += tmp,
                return

            for i in range(start, n+1):
                if n % i == 0:
                    dfs(n/i, i, tmp+[i], result)

        result = []
        dfs(n, 2, [], result)
        return result