class MinStack(object):

    # https://discuss.leetcode.com/topic/7020/java-accepted-solution-using-one-stack
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self._min = float('inf')


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self._min:
            self.stack += self._min,
            self._min = x
        self.stack += x,


    def pop(self):
        """
        :rtype: void
        """
        if self.stack.pop() == self._min:
            self._min = self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()