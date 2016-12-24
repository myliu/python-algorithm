class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # Example: [1, 2, 3]
        # [lo, hi)
        def _sort(lo, hi):
            # If there is only one element, there's nothing to sort, and the count is 0.
            # The count is 0 because we need at least two elements to get 1 count.
            if hi - lo <= 1:
                return 0

            # e.g, if prefix = [0, 1, 3, 6], mid returns index=2 (value=3)
            # Because hi is exlusive, mid is always the middle element if length is odd
            # or the one towards the right if length is even.
            mid = (lo + hi) / 2

            count = _sort(lo, mid) + _sort(mid, hi)
            i = j = mid
            for left in prefix[lo:mid]:
                while i < hi and prefix[i] - left < lower:
                    i += 1
                while j < hi and prefix[j] - left <= upper:
                    j += 1
                count += j - i
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        prefix = [0]
        for num in nums:
            prefix += prefix[-1] + num,
        return _sort(0, len(prefix))