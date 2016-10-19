class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = float('-inf')
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif num < first and num > second:
                second, third = num, second
            elif num < second and num > third:
                third = num
        return third if third != float('-inf') else first