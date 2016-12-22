class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        values = [0 for _ in range(n)]
        for i in range(n):
            for c in words[i]:
                values[i] |= 1 << ord(c) - ord('a')

        _max = 0
        for i in range(n):
            for j in range(i+1, n):
                if values[i] & values[j] == 0 and len(words[i]) * len(words[j]) > _max:
                    _max = len(words[i]) * len(words[j])
        return _max