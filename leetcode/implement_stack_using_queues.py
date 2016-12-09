from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        q = self.queue
        q += x,
        for _ in range(len(q)-1):
            q += q.popleft(),

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.queue else True