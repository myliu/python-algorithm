from collections import defaultdict

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.cache = defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.cache[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        for w in self.cache[len(word)]:
            for i, v in enumerate(word):
                if v != '.' and v != w[i]:
                    break
            else:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")