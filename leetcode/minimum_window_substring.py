from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)
        missing = len(t)
        # [left:right] are the running window boundary
        # [start:end) are the minimal window boundary
        left = right = start = end = 0
        while right < len(s):
            if need[s[right]] > 0:
                missing -= 1 
            need[s[right]] -= 1
            if not missing:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right + 1 - left < end - start:
                    start, end = left, right + 1
            right += 1
        return s[start:end]

if __name__ == '__main__':
    s = Solution()
    print s.minWindow('ADOBECODEBANC', 'ABC')