from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        for k, v in enumerate(s):
            if counter[v] == 1:
                return k

        return -1