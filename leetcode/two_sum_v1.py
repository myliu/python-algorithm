class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # key: num
        # value: index
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            if (target-num) in d:
                return [d[target-num]+1, i+1]
            d[num] = i