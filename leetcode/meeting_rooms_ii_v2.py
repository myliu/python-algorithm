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
        heap = []
        heappush(heap, (intervals[0].end, intervals[0].start))
        for interval in intervals[1:]:
            end, start = heappop(heap)
            
            if interval.start < end:
                # When there is an overlap, add the new time interval to min heap
                heappush(heap, (interval.end, interval.start))
            else:
                # When there is no overlap, merge intervals
                end = max(end, interval.end)
            heappush(heap, (end, start))
        return len(heap)