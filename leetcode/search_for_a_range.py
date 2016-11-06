class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]

            if nums[lo] <= target <= nums[hi]:
                mid = (lo+hi)/2
                left, right = search(lo, mid), search(mid+1, hi)
                return max(left, right) if -1 in left + right else [left[0], right[1]]

            return [-1, -1]

        return search(0, len(nums)-1)