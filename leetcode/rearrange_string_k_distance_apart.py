from collections import Counter
import heapq

class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        heap = [(-count, char) for char, count in Counter(str).items()]
        heapq.heapify(heap)
        res = []
        n = len(str)
        while len(res) < n:
            cur = []
            for i in range(min(max(1, k), n-len(res))):
                if not heap:
                    return ''
                count, char = heapq.heappop(heap)
                res.append(char)
                if count < -1:
                    cur.append((count+1, char))
            while cur:
                heapq.heappush(heap, cur.pop())
        return ''.join(res)