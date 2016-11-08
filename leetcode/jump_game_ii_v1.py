class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_max_jump = current_max_jump = jumps = 0
        for k, v in enumerate(nums[:-1]):
            current_max_jump = max(current_max_jump, k+v)
            if k == last_max_jump:
                last_max_jump = current_max_jump
                jumps += 1
        return jumps