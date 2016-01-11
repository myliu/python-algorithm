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
            l, r = 0, i - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum < t:
                    count += r - l
                    l += 1
                else:
                    r -= 1
        return count

if __name__ == '__main__':
    s = Solution()
    print s.threeSumSmaller([0,0,0], 0)
    print s.threeSumSmaller([1,1,-2], 1)
    print s.threeSumSmaller([-2, 0, 1, 3], 2)