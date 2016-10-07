import random

class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        result = -1
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            if random.randint(0, count) == 0:
                result = i
            count += 1
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)