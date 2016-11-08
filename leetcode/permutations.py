class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(candidates, tmp, result):
            if not candidates:
                result += tmp,
                return

            for i in range(len(candidates)):
                helper(candidates[:i]+candidates[i+1:], tmp+[candidates[i]], result)

        result = []
        helper(nums, [], result)
        return result