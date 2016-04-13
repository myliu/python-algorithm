class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False

        d = {}
        w = t + 1
        for i, n in enumerate(nums):
            if i > k:
                del d[nums[i-k-1]/w]
            
            m = n / w
            if m in d:
                return True
            if m - 1 in d and abs(n - d[m-1]) < w:
                return True
            if m + 1 in d and abs(n - d[m+1]) < w:
                return True

            d[m] = n

        return False