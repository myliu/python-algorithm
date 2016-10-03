class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def dfs(k, result):
            if k > n:
                return
            result.append(k)

            t = k * 10
            if t > n:
                return
            
            for i in range(10):
                if t + i <= n:
                    dfs(t+i, result)

        result = []
        for k in range(1, 10):
            dfs(k, result)
        return result