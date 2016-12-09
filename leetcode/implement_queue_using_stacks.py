class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.input += x,

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.output.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.output:
            while self.input:
                self.output += self.input.pop(),
        return self.output[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.input or self.output)