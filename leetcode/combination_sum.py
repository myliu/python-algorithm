class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(remaining, path, res):
            if remaining == 0:
                res.add(path)
                    
            for c in candidates:
                if remaining >= c:
                    helper(remaining-c, path+(c,), res)

        res = set()
        helper(target, (), res)
        return map(list, set(tuple(sorted(path)) for path in res))