class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        acc, ans = 0, 0
        d = {0:-1}
        for i in xrange(len(nums)):
            acc += nums[i]
            if acc not in d:
                d[acc] = i
            if acc-k in d:
                ans = max(ans, i-d[acc-k])
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [1, -1, 5, -2, 3]
    print s.maxSubArrayLen(nums, 3)