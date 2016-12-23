class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:-1}
        _sum, _max = 0, 0
        for i, num in enumerate(nums):
            _sum += num
            if _sum not in d:
                d[_sum] = i
            if _sum - k in d:
                _max = max(_max, i - d[_sum - k])
        return _max

if __name__ == '__main__':
    s = Solution()
    nums = [1, -1, 5, -2, 3]
    print s.maxSubArrayLen(nums, 3)