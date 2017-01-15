# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(lo, hi):
            if lo + 1 >= hi:
                return lo if isBadVersion(lo) else hi

            mid = lo + (hi - lo) / 2
            if isBadVersion(mid):
                return helper(lo, mid)
            return helper(mid+1, hi)

        return helper(1, n)