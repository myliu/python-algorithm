from collections import deque

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = deque()
        if v1:
            self.queue += (len(v1), iter(v1)),
        if v2:
            self.queue += (len(v2), iter(v2)),

    def next(self):
        """
        :rtype: int
        """
        _len, _iter = self.queue.popleft()
        if _len > 1:
            self.queue += (_len-1, _iter),
        return _iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.queue)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())