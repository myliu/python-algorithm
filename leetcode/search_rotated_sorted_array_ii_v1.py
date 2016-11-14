class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end-start)/2

            if nums[mid] == target:
                return True

            while nums[start] == nums[mid] and start != mid:
                start += 1

            while nums[mid] == nums[end] and mid != end:
                end -= 1

            if nums[start] <= nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False