# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):

    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s:
            return None

        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        cur = None
        l = 0
        for k, v in enumerate(s):
            if v == '[':
                if cur:
                   stack.append(cur)
                cur = NestedInteger()
                l = k + 1
            elif v == ']':
                num = s[l:k]
                if num:
                    cur.add(NestedInteger(int(num)))
                if stack:
                    pop = stack.pop()
                    pop.add(cur)
                    cur = pop
                l = k + 1
            elif v == ',':
                if s[k-1] != ']':
                    num = s[l:k]
                    cur.add(NestedInteger(int(num)))
                l = k + 1
        return cur