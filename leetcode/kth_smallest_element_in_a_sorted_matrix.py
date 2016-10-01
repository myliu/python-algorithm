import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(v, 0, j) for j, v in enumerate(matrix[0])]
        heapq.heapify(heap)
        for _ in range(k):
            v, i, j = heapq.heappop(heap)
            if i + 1 < len(matrix):
                next_element = (matrix[i+1][j], i+1, j)
                heapq.heappush(heap, next_element)
        return v