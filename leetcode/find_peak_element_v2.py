class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def search(nums, left, right):
            if left + 1 >= right:
                return left if nums[left] > nums[right] else right

            mid = (left + right) / 2
            if nums[mid] == max(nums[mid-1:mid+2]):
                return mid
            elif nums[mid-1] == max(nums[mid-1:mid+2]):
                return search(nums, left, mid-1)
            else:
                return search(nums, mid+1, right)

        return search(nums, 0, len(nums)-1)