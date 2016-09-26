from bisect import bisect_left

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x:(x[0],-x[1]))
        heights = [float('inf')] + [0] * (len(envelopes)-1)
        max_idx = 0
        for width, height in envelopes:
            idx = bisect_left(heights, height, hi=max_idx+1)
            heights[idx] = height
            max_idx = max(max_idx, idx)
        return max_idx+1