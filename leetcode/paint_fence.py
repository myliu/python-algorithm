class Solution(object):

    # https://discuss.leetcode.com/topic/23426/o-n-time-java-solution-o-1-space
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        # n == 2
        diff = k * (k-1)
        same = k
        # n >= 3
        for i in range(2, n):
            diff, same = (same + diff) * (k - 1), diff
        return diff + same