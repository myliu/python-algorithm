class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1 = idx2 = -1
        _min = float('inf')
        for i, word in enumerate(words):
            if word == word1:
                if idx2 != -1:
                    _min = min(_min, i - idx2)
                idx1 = i
            elif word == word2:
                if idx1 != -1:
                    _min = min(_min, i - idx1)
                idx2 = i
        return _min