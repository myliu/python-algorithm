class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        d = {}
        m = i = j = 0
        while i < len(s):
            c = s[i]
            if c in d:
                j = max(j, d[c]+1)

            d[c] = i
            m = max(m, i-j+1)
            i += 1
        return m