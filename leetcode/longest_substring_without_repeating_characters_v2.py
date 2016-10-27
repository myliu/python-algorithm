from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        l = r = _max = 0
        window = defaultdict(int)
        while l < n:
            while r < n and s[r] not in window:
                _max = max(_max, r-l+1)
                window[s[r]] += 1
                r += 1

            window[s[l]] -= 1
            if not window[s[l]]:
                del window[s[l]]
            l += 1
        return _max