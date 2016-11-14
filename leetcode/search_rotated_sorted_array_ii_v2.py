class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.helper(nums, target, 0, len(nums)-1)

    def helper(self, nums, target, left, right):
        if left + 1 >= right:
            if target in (nums[left], nums[right]):
                return True
            else:
                return False

        mid = (left + right) / 2
        
        while nums[left] == nums[mid] and left != mid:
            left += 1

        while nums[right] == nums[mid] and right != mid:
            right -= 1

        if nums[left] <= nums[mid]:
            if target >= nums[left] and target <= nums[mid]:
                return self.helper(nums, target, left, mid)
            else:
                return self.helper(nums, target, mid+1, right)
        else:
            if target >= nums[mid] and target <= nums[right]:
                return self.helper(nums, target, mid, right)
            else:
                return self.helper(nums, target, left, mid-1)