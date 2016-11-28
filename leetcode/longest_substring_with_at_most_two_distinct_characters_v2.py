from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        window = defaultdict(int)
        left = right = 0
        longest = 0
        while right < n:
            window[s[right]] += 1
            if len(window) <= 2:
                longest = max(longest, right-left+1)
                right += 1
                continue
            while left <= right and len(window) > 2:
                window[s[left]] -= 1
                if not window[s[left]]:
                    del window[s[left]]
                left += 1
            right += 1
        return longest