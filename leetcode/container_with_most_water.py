class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        _max = 0
        left, right = 0, len(height) - 1
        while left < right:
            _max = max(_max, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return _max