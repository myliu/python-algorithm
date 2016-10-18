from collections import Counter

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        counter = Counter()

        # [lo, hi): lo is inclusive, and hi is exclusive
        hi = lo = 0
        for hi in range(1, n+1):
            counter[s[hi-1]] += 1
            if hi - lo - counter.most_common(1)[0][1] > k:
                counter[s[lo]] -= 1
                lo += 1
        return hi - lo