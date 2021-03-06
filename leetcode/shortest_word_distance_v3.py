class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        _min = float('inf')
        idx1 = idx2 = -1
        for i, word in enumerate(words):
            if word == word1:
                idx1 = i
            elif word == word2:
                idx2 = i

            if idx1 != -1 and idx2 != -1:
                _min = min(_min, abs(idx1 - idx2))
        return _min