class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.word = None

class Solution(object):

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = self.build_trie(words)
        res = []
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, root, res)
        return res


    def dfs(self, board, x, y, trie, res):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return

        c = board[x][y]

        if c == '*' or c not in trie.children:
            return

        child = trie.children[c]
        if child.word is not None:
            res.append(child.word)
            child.word = None

        board[x][y] = '*'
        self.dfs(board, x-1, y, child, res)
        self.dfs(board, x, y-1, child, res)
        self.dfs(board, x+1, y, child, res)
        self.dfs(board, x, y+1, child, res)
        board[x][y] = c


    def build_trie(self, words):
        root = TrieNode()
        for word in words:
            current = root
            for i in word:
                if i not in current.children:
                    current.children[i] = TrieNode()
                current = current.children[i]
            current.word = word
        return root
