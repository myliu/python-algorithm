from collections import defaultdict

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.d = defaultdict(list)
        for i, word in enumerate(words):
            self.d[word] += i,


    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = self.d
        indexes1, indexes2 = d[word1], d[word2]
        i = j = 0
        _min = float('inf')
        while i < len(indexes1) and j < len(indexes2):
            _min = min(_min, abs(indexes1[i]-indexes2[j]))
            if indexes1[i] < indexes2[j]:
                i += 1
            else:
                j += 1
        return _min


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")