class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        n = len(height)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        result = 0
        for i in range(1, n-1):
            result += max(0, min(left[i-1], right[i+1]) - height[i])
        return result