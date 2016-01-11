from sys import maxint

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = maxint
        nums.sort()
        for i in range(2, len(nums)):
            t = target - nums[i]
            l, r = 0, i - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == t:
                    return target
                elif sum > t:
                    r -= 1
                else:
                    l += 1
                if abs(t - sum) < abs(target - closest):
                    closest = sum + nums[i]
        return closest

if __name__ == '__main__':
    s = Solution()
    print s.threeSumClosest([1, 1, 1, 0], 100)