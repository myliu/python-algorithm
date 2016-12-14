class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        n = len(citations)
        counts = [0 for _ in range(n+1)]

        for citation in citations:
            counts[min(citation, n)] += 1

        count = 0
        for i in range(n, -1, -1):
            count += counts[i]
            if count >= i:
                return i