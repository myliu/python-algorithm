class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for k, v in enumerate(nums):
            if k > reach:
                return False
            reach = max(reach, k+v)
        return True