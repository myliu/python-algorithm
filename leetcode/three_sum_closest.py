class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = float('inf')
        nums.sort()
        for i in range(2, len(nums)):
            t = target - nums[i]
            left, right = 0, i - 1
            while left < right:
                _sum = nums[left] + nums[right]
                if _sum == t:
                    return target
                elif _sum > t:
                    right -= 1
                else:
                    left += 1
                if abs(t - _sum) < abs(target - closest):
                    closest = _sum + nums[i]
        return closest

if __name__ == '__main__':
    s = Solution()
    print s.threeSumClosest([1, 1, 1, 0], 100)