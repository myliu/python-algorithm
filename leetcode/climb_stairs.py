class Solution(object):

    def __init__(self):
        self.cache = {1:1, 2:2}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.cache:
            self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.cache[n]