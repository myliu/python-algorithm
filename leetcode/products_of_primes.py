class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, 0, 1, result)
        return result

    def dfs(self, nums, start, tmp, result):
        result += tmp,
        
        for i in range(start, len(nums)):
            self.dfs(nums, i+1, tmp*nums[i], result)

if __name__ == '__main__':
    s = Solution()
    nums = [2, 11, 3]
    print s.subsets(nums)