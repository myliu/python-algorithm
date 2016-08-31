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
        q.append(x)
        for i in range(len(q)-1):
            q.append(q.popleft())


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
        if self.queue:
            return False
        else:
            return True