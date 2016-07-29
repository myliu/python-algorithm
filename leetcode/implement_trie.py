import collections

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for i in word:
            current = current.children[i]
        current.is_word = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for i in word:
            if not i in current.children:
                return False
            current = current.children[i]
        return current.is_word


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for i in prefix:
            if not i in current.children:
                return False
            current = current.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")