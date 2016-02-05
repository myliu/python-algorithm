import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []
        for b in buildings:
            points.append((b[0], -b[2]))
            points.append((b[1], b[2]))
        points.sort(key=lambda x: (x[0], x[1]))

        # Current height
        prev = 0
        pq = [0]
        results = []
        for p in points:
            if p[1] < 0:
                heapq.heappush(pq, p[1])
            else:
                if -p[1] in pq:
                    pq.remove(-p[1])
                    heapq.heapify(pq)

            current = -pq[0]
            if prev != current:
                results.append((p[0], current))
                prev = current
        return results