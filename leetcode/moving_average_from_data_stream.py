from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        window = self.window
        window += val,
        return float(sum(window)) / len(window)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)