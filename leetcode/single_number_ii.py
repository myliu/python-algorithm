class Solution(object):

    # https://discuss.leetcode.com/topic/2926/accepted-code-with-proper-explaination-does-anyone-have-a-better-idea
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            common_bit_mask = ~ (ones & twos)
            ones &= common_bit_mask
            twos &= common_bit_mask
        return ones