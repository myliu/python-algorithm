class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        count = 1
        for num in nums[1:]:
            if not count:
                majority = num
                count = 1
            elif num == majority:
                count += 1
            else:
                count -= 1
        return majority

if __name__ == '__main__':
    s = Solution()
    num = [1, 2, 3, 2, 2]
    print s.majorityElement(num)