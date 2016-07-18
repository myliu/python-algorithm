# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import collections

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)

        result = 0

        for i in xrange(len(points)):
            # Key: Slope
            # Value: Count
            d = collections.defaultdict(int)
            overlap = 0

            for j in xrange(i+1, len(points)):
                dx, dy = points[i].x - points[j].x, points[i].y - points[j].y
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                slope = dy * 1.0 / dx if dx != 0 else 'infinity'
                d[slope] += 1

            curmax = max(d.values()) if d else 0
            result = max(result, curmax + overlap + 1)

        return result