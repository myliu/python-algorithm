class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(2, len(nums)):
            t = target - nums[i]
            left, right = 0, i - 1
            while left < right:
                _sum = nums[left] + nums[right]
                if _sum < t:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count

if __name__ == '__main__':
    s = Solution()
    print s.threeSumSmaller([0,0,0], 0)
    print s.threeSumSmaller([1,1,-2], 1)
    print s.threeSumSmaller([-2, 0, 1, 3], 2)