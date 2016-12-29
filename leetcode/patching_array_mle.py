class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        def dfs(nums, pos, tmp, result):
            if pos == len(nums):
                if tmp:
                    result.add(sum(tmp))
                return

            dfs(nums, pos+1, tmp, result)
            for i in range(pos, len(nums)):
                dfs(nums, i+1, tmp+[nums[i]], result)

        result = set()
        dfs(nums, 0, [], result)

        patch = []
        for i in range(1, n+1):
            if i not in result:
                patch += i,
                result = result.union(set(map(lambda x: x+i, result)))
        return len(patch)