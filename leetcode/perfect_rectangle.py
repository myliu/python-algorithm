from collections import Counter

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        m1, n1, m2, n2 = float('inf'), float('inf'), float('-inf'), float('-inf')
        area = 0
        counter = Counter()
        for x1, y1, x2, y2 in rectangles:
            m1 = min(m1, x1)
            n1 = min(n1, y1)
            m2 = max(m2, x2)
            n2 = max(n2, y2)
            area += (x2-x1)*(y2-y1)
            
            counter[(x1, y1)] += 1
            counter[(x1, y2)] += 1
            counter[(x2, y1)] += 1
            counter[(x2, y2)] += 1

        corners = Counter({(m1,n1):1, (m1,n2):1, (m2,n1):1, (m2,n2):1})
        for count in (counter-corners).values():
            if count % 2 == 1:
                return False

        return area == (m2-m1)*(n2-n1)