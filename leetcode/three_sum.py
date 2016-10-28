class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) <= 2:
            return []

        results = set()
        nums.sort()
        for i in range(2, len(nums)):
            target = 0 - nums[i]
            left, right = 0, i - 1
            while left < right:
                _sum = nums[left] + nums[right]
                if _sum == target:
                    results.add((nums[left], nums[right], nums[i]))
                    left += 1
                elif _sum > target:
                    right -= 1
                else:
                    left += 1
        return map(list, results)

if __name__ == '__main__':
    s = Solution()
    print s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
    # Output: [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]