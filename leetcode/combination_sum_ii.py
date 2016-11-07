class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # target: the target at current level, which will keep decreasing until 0
        # candidates: the sorted candidates
        # start: the index of candidates at current level
        # path: a tuple that keeps track of the current result
        def helper(candidates, target, start, path, result):
            if target == 0:
                result.append(path)
                return
            
            for i in range(start, len(candidates)):
                c = candidates[i]
                
                if i > start and c == candidates[i-1]:
                    continue
                
                if target >= c:
                    helper(candidates, target-c, i+1, path+(c,), result)
            
        result = []
        helper(sorted(candidates), target, 0, (), result)
        return result