from collections import defaultdict

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.d[len(word)].add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        for w in self.d[len(word)]:
            for i, c in enumerate(word):
                if c != '.' and c != w[i]:
                    break
            else:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")