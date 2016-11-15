class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights += 0,
        # 'stack' holds the index
        # Elements on the stack are monotonically increased.
        stack = [0]
        _max = 0

        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                _max = max(_max, height * width)
            stack += i,
        return _max