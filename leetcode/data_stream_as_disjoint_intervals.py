# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from heapq import *

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        heappush(self.intervals, (val, Interval(val, val)))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        stack = []
        while self.intervals:
            idx, interval = heappop(self.intervals)
            if not stack:
                stack += (idx, interval),
            else:
                _, prev = stack[-1]
                if prev.end + 1 >= interval.start:
                    prev.end = max(prev.end, interval.end)
                else:
                    stack += (idx, interval),
        self.intervals = stack
        return map(lambda x: x[1], stack)


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()