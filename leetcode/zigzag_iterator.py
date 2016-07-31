import itertools

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.cache = [x for v in itertools.izip_longest(v1, v2) for x in v if x is not None][::-1]


    def next(self):
        """
        :rtype: int
        """
        return self.cache.pop()


    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.cache)


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())