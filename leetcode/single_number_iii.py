class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # diff is XOR of the two distinct numbers
        diff = 0
        for num in nums:
            diff ^= num

        # diff is the last set bit
        diff &= -diff

        num0 = num1 = 0
        for num in nums:
            if num & diff == 0:
                num0 ^= num
            else:
                num1 ^= num
        return [num0, num1]