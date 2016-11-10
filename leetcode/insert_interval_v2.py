# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import *

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        heap = []

        for interval in intervals:
            heappush(heap, (interval.start, interval))
        heappush(heap, (newInterval.start, newInterval))

        stack = []
        while heap:
            start, interval = heappop(heap)
            if not stack:
                stack += (start, interval),
            else:
                _, prev = stack[-1]
                if prev.end >= start:
                    prev.end = max(prev.end, interval.end)
                else:
                    stack += (start, interval),

        return map(lambda x:x[1], stack)