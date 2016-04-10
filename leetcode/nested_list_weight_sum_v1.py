class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def helper(nestedList, depth):
            sum = 0
            for item in nestedList:
                if item.isInteger():
                    sum += depth * item.getInteger()
                else:
                    next_list = item.getList()
                    sum += helper(next_list, depth+1)
            return sum
        return helper(nestedList, 1)