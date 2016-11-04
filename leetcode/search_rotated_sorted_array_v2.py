class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.helper(nums, target, 0, len(nums)-1)

    def helper(self, nums, target, left, right):
        if left + 1 >= right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1

        mid = (left + right) / 2
        if nums[left] <= nums[mid]:
            if target >= nums[left] and target <= nums[mid]:
                return self.helper(nums, target, left, mid)
            else:
                return self.helper(nums, target, mid, right)
        else:
            if target >= nums[mid] and target <= nums[right]:
                return self.helper(nums, target, mid, right)
            else:
                return self.helper(nums, target, left, mid)