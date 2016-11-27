# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)

        if n <= 2:
            return n

        _max = 0
        for i in range(n):
            # Key: Slope
            # Value: Count
            slopes = defaultdict(int)
            overlap = 0

            for j in range(i+1, n):
                pi, pj = points[i], points[j]
                dx, dy = pi.x-pj.x, pi.y-pj.y

                if not dx and not dy:
                    overlap += 1
                    continue

                slope = dy * 1.0 / dx if dx else float('inf')
                slopes[slope] += 1

            running_max = max(slopes.values()) if slopes else 0
            _max = max(_max, running_max + overlap + 1)

        return _max