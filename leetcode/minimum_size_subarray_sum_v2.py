class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        left = right = 0
        _sum = 0
        min_len = float('inf')

        while right < n:
            _sum += nums[right]

            while _sum >= s:
                min_len = min(min_len, right-left+1)
                _sum -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != float('inf') else 0