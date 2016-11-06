class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(target, path, result):
            if target == 0:
                result.add(path)
                return

            for c in candidates:
                if target >= c:
                    helper(target-c, path+(c,), result)

        result = set()
        helper(target, (), result)
        return map(list, set(tuple(sorted(path)) for path in result))