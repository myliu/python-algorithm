from collections import defaultdict

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.d = defaultdict(list)
        for i, v in enumerate(words):
            self.d[v].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1 = self.d[word1]
        list2 = self.d[word2]
        i, j, res = 0, 0, float('inf')
        while i < len(list1) and j < len(list2):
            res = min(res, abs(list1[i]-list2[j]))
            if list1[i] < list2[j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")