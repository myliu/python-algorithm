class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        while j >= 0:
            if i < 0 or nums2[j] > nums1[i]:
                nums1[i+j+1] = nums2[j]
                j -= 1
            else:
                nums1[i+j+1] = nums1[i]
                i -= 1