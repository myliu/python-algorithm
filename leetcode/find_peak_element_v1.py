class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary_search(nums, i, j):
            if i == j:
                return i

            mid1 = i + (j-i)/2
            mid2 = mid1 + 1
            if nums[mid1] > nums[mid2]:
                return binary_search(nums, i, mid1)
            else:
                return binary_search(nums, mid2, j)

        return binary_search(nums, 0, len(nums)-1)