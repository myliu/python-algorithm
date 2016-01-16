# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import operator

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals or len(intervals) <= 1:
            return True

        intervals.sort(key=operator.attrgetter('start'))
        # Verbose
        # for i in range(1, len(intervals)):
        #     if intervals[i].start < intervals[i-1].end:
        #         return False
        # return True

        # Concise
        return not any([intervals[i-1].end > intervals[i].start for i in xrange(1, len(intervals))])