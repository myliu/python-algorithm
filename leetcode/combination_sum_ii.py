class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # target is the target at current level, which will keep decreasing until 0
        # candidates is the sorted candidates
        # start is the index of candidates at current level
        # path is a tuple that keeps track of the current result
        def helper(target, candidates, start, path, res):
            if target == 0:
                res.append(path)

            for i in range(start, len(candidates)):
                c = candidates[i]

                if i > start and c == candidates[i-1]:
                    continue

                if target >= c:
                    helper(target-c, candidates, i+1, path+(c,), res)

        res = []
        helper(target, sorted(candidates), 0, (), res)
        return res