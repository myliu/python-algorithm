class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = running_sum = nums[0]
        for num in nums[1:]:
            running_sum = max(num, num + running_sum)
            max_sum = max(running_sum, max_sum)
        return max_sum

if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print s.maxSubArray(nums)