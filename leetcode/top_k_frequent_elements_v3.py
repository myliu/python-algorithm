from collections import Counter
from heapq import heappush, heappop

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        heap = []
        for key, value in counter.items():
            heappush(heap, (-value, key))

        result = []
        for _ in range(k):
            result += heappop(heap)[1],
        return result