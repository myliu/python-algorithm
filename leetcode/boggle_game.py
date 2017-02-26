from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = self.build_trie(words)
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, '', result)
        return result

    def build_trie(self, words):
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                curr = curr.children[c]
            curr.is_word = True
        return root

    def dfs(self, board, i, j, node, tmp, result):
        m, n = len(board), len(board[0])
        
        if i < 0 or i >= m or j < 0 or j >= n:
            return

        c = board[i][j]
        if c == '*' or c not in node.children:
            return

        child = node.children[c]
        if child.is_word:
            result += tmp + c,
            child.is_word = False

        board[i][j] = '*'
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            self.dfs(board, i+dx, j+dy, child, tmp + c, result)
        board[i][j] = c

if __name__ == '__main__':
    # board = [['G','I','Z'],
    #          ['U','E','K'],
    #          ['Q','S','E']]
    # words = ["GEEKS", "FOR", "QUIZ", "GO"]
    board = [['a', 'b', 'c'],
             ['d', 'e', 'f'],
             ['g', 'h', 'i']]
    words = ["abce", "cfi", "beh", "defi", "gh", "gda"]
    s = Solution()
    print s.findWords(board, words)