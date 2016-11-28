class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(nums, 0, len(nums)-1)

    def search(self, nums, left, right):
        if left + 1 >= right:
            return min(nums[left], nums[right])

        mid = (left + right) / 2
        if nums[mid] > nums[right]:
            return self.search(nums, mid+1, right)
        elif nums[mid] < nums[right]:
            return self.search(nums, left, mid)
        else:
            return self.search(nums, left, right-1)