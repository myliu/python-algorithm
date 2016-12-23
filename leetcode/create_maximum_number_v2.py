class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def prep(nums, k):
            n = len(nums)
            drop = n - k
            result = []
            for num in nums:
                while drop and result and result[-1] < num:
                    result.pop()
                    drop -= 1
                result += num,
            return result[:k]

        def merge(nums1, nums2, k):
            return [max(nums1, nums2).pop(0) for _ in range(k)]

        _max = []
        for i in range(k+1):
            if i <= len(nums1) and k-i <= len(nums2):
                _max = max(_max, merge(prep(nums1, i), prep(nums2, k-i), k))
        return _max