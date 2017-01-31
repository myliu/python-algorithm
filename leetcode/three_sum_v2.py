class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        n =  len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                if left > i + 1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if nums[i] + nums[left] + nums[right] == 0:
                    results += [nums[i], nums[left], nums[right]],
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return results