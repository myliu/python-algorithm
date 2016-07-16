import collections

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque([])


    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.q.append(timestamp)


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        q = self.q
        while q:
            if timestamp - q[0] >= 300:
                q.popleft()
            else:
                break
        return len(q)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)