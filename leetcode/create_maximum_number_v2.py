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
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(nums1, nums2, k):
            return [max(nums1, nums2).pop(0) for _ in range(k)]
        
        return max(merge(prep(nums1, i), prep(nums2, k-i), k)
                for i in range(k+1)
                if i <= len(nums1) and k-i <= len(nums2))