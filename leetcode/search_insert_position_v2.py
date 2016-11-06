class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def search(lo, hi):
            if lo + 1 >= hi:
                if target > nums[hi]:
                    return hi + 1
                elif target == nums[hi]:
                    return hi
                elif target > nums[lo]:
                    return lo + 1
                else:
                    return lo

            mid = (lo + hi) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return search(lo, mid-1)
            else:
                return search(mid+1, hi)

        return search(0, len(nums)-1)