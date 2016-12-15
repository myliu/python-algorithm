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
        return self.helper(1, n)
        
    def helper(self, m, n):
        if m == n:
            return m

        mid = m + (n-m)/2
        if not isBadVersion(mid):
            return self.helper(mid+1, n)
        return self.helper(m, mid)