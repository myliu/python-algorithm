class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = p2 = -1
        m = float("inf")
        if word1 == word2:
            for i in range(len(words)):
                if words[i] == word1:
                    if p1 == -1:
                        p1 = i
                    else:
                        m = min(m, i-p1)
                        p1 = i
        else:
            for i in range(len(words)):
                if words[i] == word1:
                    p1 = i
                if words[i] == word2:
                    p2 = i
                if p1 != -1 and p2 != -1:
                    m = min(m, abs(p1-p2))
        return m