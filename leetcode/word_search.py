class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def helper(board, x, y, word, i):
            if i == len(word):
                return True

            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[i]:
                return False

            tmp = board[x][y]
            board[x][y] = '*'
            res = helper(board, x-1, y, word, i+1) or helper(board, x+1, y, word, i+1) or helper(board, x, y-1, word, i+1) or helper(board, x, y+1, word, i+1)
            board[x][y] = tmp
            return res

        return any(helper(board, i, j, word, 0) for j in xrange(len(board[0])) for i in xrange(len(board)))