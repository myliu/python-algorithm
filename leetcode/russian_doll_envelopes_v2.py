class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def compare(x, y):
            if x[0] < y[0] or (x[0] == y[0] and x[1] > y[1]):
                return -1
            else:
                return 1

        if not envelopes:
            return 0

        envelopes.sort(cmp=compare)
        n = len(envelopes)
        liss = [1] * n
        for i in range(1, n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    liss[i] = max(liss[i], liss[j]+1)
        return max(liss)