class Solution(object):

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = [] 
        self.combination(k, n, 1, [], results)
        return results

    def combination(self, k, n, start, tmp, results):
        if n < 0:
            return

        if len(tmp) == k and n == 0:
            results.append(tmp)
            return

        for i in range(start, 10):
            self.combination(k, n-i, i+1, (tmp+[i]), results)