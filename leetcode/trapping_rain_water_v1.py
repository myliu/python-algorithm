class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = [0] * len(height)
        right = [0] * len(height)

        max_height = 0
        for i in xrange(1, len(height)):
            left[i] = max_height = max(max_height, height[i-1])

        max_height = 0
        for i in xrange(len(height)-2, -1, -1):
            right[i] =max_height = max(max_height, height[i+1])

        trapped = 0
        for i in xrange(len(height)):
            min_wall = min(left[i], right[i])
            if min_wall > height[i]:
                trapped += min_wall - height[i]

        return trapped