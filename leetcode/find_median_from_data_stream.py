from heapq import *

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small, self.large = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        small, large = self.small, self.large
        heappush(small, -heappushpop(large, num))
        if len(small) > len(large):
            heappush(large, -heappop(small))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        small, large = self.small, self.large
        if len(large) > len(small):
            return float(large[0])
        else:
            return float(large[0]-small[0])/2

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()