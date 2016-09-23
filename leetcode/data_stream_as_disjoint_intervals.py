import heapq

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

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
        heapq.heappush(self.intervals, (val, Interval(val, val)))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        stack = []
        while self.intervals:
            idx, val = heapq.heappop(self.intervals)
            if not stack:
                stack.append((idx, val))
            else:
                _, prev = stack[-1]
                if prev.end + 1 >= val.start:
                    prev.end = max(prev.end, val.end)
                else:
                    stack.append((idx, val))
        self.intervals = stack
        return map(lambda x: x[1], stack)


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()