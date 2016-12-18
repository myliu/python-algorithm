class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]

        # To find the meeting point.
        # https://discuss.leetcode.com/topic/19367/java-o-1-space-solution-with-detailed-explanation/24
        # Distance to meeting point for fast pointer a + b + (b + c)
        # Distance to meeting point for slow pointer a + b
        # a + b + (b + c) = 2(a + b)
        # c = a
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # To find the entry point, which is the duplicate number.
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow