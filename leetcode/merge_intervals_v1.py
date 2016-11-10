# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from operator import attrgetter

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        stack = []
        intervals.sort(key=attrgetter('start'))
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                prev = stack[-1]
                if interval.start <= prev.end:
                    prev.end = max(prev.end, interval.end)
                else:
                    stack.append(interval)
        return stack