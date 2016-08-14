class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = reach = jumps = 0
        for k, v in enumerate(nums[:-1]):
            reach = max(reach, k+v)
            if k == end:
                end = reach
                jumps += 1
        return jumps