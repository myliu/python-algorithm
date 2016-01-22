import sys

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist = sys.maxint
        for i in range(len(words)):
            if words[i] != word1:
                continue

            for j in range(len(words)):
                if words[j] == word2:
                    dist = min(dist, abs(i-j))
        return dist