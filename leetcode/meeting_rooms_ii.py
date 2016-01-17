# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        s = e = 0
        numRooms = available = 0
        while s < len(starts):
            print 'start:{} end:{} numRooms:{} available:{}'.format(starts[s], ends[e], numRooms, available)
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1
        return numRooms

if __name__ == '__main__':
    s = Solution()
    i1 = Interval(0,8)
    i2 = Interval(5,10)
    i3 = Interval(9, 11)
    intervals = [i1, i2, i3]
    print s.minMeetingRooms(intervals)

    # start:0 end:8 numRooms:0 available:0
    # start:5 end:8 numRooms:1 available:0
    # start:9 end:8 numRooms:2 available:0
    # start:9 end:10 numRooms:2 available:1
    # 2
