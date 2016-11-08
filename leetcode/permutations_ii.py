class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(candidates, tmp, result):
            if not candidates:
                result += tmp,
                return

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                helper(candidates[:i]+candidates[i+1:], tmp+[candidates[i]], result)

        result = []
        helper(sorted(nums), [], result)
        return result