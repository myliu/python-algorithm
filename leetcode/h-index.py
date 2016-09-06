class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        n = len(citations)
        counts = dict.fromkeys(range(n+1), 0)
        
        for citation in citations:
            for i in range(min(n, citation)+1):
                counts[i] += 1

        return max(min(k,v) for k, v in counts.items())