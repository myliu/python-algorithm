class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = [float('inf')]


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.minimum[0]:
            self.stack.append(self.minimum[0])
            self.minimum[0] = x
        self.stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        top = self.stack.pop()
        if top == self.minimum[0]:
            self.minimum[0] = self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()