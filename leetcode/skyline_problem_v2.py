from heapq import *

# Final
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []
        for left, right, height in buildings:
            points += (left, -height),
            points += (right, height),

        points.sort()

        heap = [0]
        prev = 0

        results = []
        for x, y in points:
            if y < 0:
                heappush(heap, y)
            else:
                # Intuitive solution
                # heap.remove(-y)
                # heapify(heap)

                # Accepted solution
                if -y == heap[-1]:
                    heap.pop()
                else:
                    i = heap.index(-y)
                    heap[i] = heap[-1]
                    heap.pop()
                    heapq._siftup(heap, i)

            current = -heap[0]

            if prev != current:
                results += [x, current],
                prev = current

        return results