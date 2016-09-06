class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        n = len(citations)
        l, r = 0, n-1
        while l + 1 < r:
            mid = l + (r-l)/2
            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] > n - mid:
                r = mid
            else:
                l = mid
        return max(min(citations[l], n-l), min(citations[r], n-r))