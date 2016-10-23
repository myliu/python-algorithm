from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m, n = len(s), len(p)
        p_counter = Counter(p)
        s_counter = Counter(s[:n-1])
        results = []
        for i in range(n-1, m):
            s_counter[s[i]] += 1
            if p_counter == s_counter:
                results += i-(n-1),
            window_start = s[i-(n-1)]
            s_counter[window_start] -= 1
            if s_counter[window_start] == 0:
                del s_counter[window_start]
        return results