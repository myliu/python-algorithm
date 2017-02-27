class Solution(object):

    # https://discuss.leetcode.com/topic/27608/java-python-one-pass-solution-o-n-time-o-n-space-using-buckets
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False

        buckets = {}
        n = len(nums)
        w = t + 1
        for i, num in enumerate(nums):
            print i, num, buckets
            b = num / w
            if b in buckets:
                return True
            if b-1 in buckets and abs(num - buckets[b-1]) <= t:
                return True
            if b+1 in buckets and abs(num - buckets[b+1]) <= t:
                return True

            buckets[b] = num

            # Note: It is impossible that two numbers between index i-k and i are sharing the same bucket.
            # If that is the case, we would have returned True already.
            # Example: i = 5, k = 5, i - k = 0
            if i >= k:
                del buckets[nums[i-k]/w]
        return False

if __name__ == '__main__':
    s = Solution()
    nums = [1, 4, 8, 5]
    print s.containsNearbyAlmostDuplicate(nums, 3, 2)