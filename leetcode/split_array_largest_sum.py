class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def binary_search(nums, m, lo, hi):
            while lo + 1 < hi:
                mid = (lo + hi) / 2
                if is_valid(nums, m, mid):
                    hi = mid
                else:
                    lo = mid
            if is_valid(nums, m, lo):
                return lo
            else:
                return hi

        def is_valid(nums, m, mx):
            count = 1
            current = 0
            for num in nums:
                current += num
                if current > mx:
                    count += 1
                    if count > m:
                        return False
                    current = num
            return True

        return binary_search(nums, m, max(nums), sum(nums))