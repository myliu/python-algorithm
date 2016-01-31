class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_sum = small = large = nums[0]
        for num in nums[1:]:
            large, small = max(num, num * large, num * small), min(num, num * large, num * small)
            max_sum = max(large, max_sum)
        return max_sum

if __name__ == '__main__':
    s = Solution()
    nums = [-2, 3, -4]
    print s.maxProduct(nums)