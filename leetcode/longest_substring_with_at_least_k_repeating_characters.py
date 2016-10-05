class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for ch in s:
            if s.count(ch) < k:
                return max(self.longestSubstring(token, k) for token in s.split(ch))
        return len(s)