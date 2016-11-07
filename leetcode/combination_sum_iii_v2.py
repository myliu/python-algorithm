class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(candidates, target, start, path, result):
            if len(path) == k:
                if target == 0:
                    result.append(path)
                return

            for i in range(start, len(candidates)):
                c = candidates[i]
                
                if target >= c:
                    helper(candidates, target-c, i+1, path+(c,), result)

        result = []
        helper(range(1, 10), n, 0, (), result)
        return result