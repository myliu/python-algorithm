# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq

class Solution(object):
    
    # https://discuss.leetcode.com/topic/20958/ac-java-solution-using-min-heap
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)
        n = len(intervals)
        heap = []
        heapq.heappush(heap, (intervals[0].end, intervals[0].start))
        for i in range(1, n):
            end, start = heapq.heappop(heap)

            # When there is no overlap, merge intervals
            if intervals[i].start >= end:
                end = intervals[i].end
            # When there is an overlap, add the new time interval to min heap
            else:
                heapq.heappush(heap, (intervals[i].end, intervals[i].start))

            heapq.heappush(heap, (end, start))
        return len(heap)