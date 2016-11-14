class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        return any(self.dfs(board, i, j, word, 0) for i in range(len(board)) for j in range(len(board[0])))

    def dfs(self, board, x, y, word, start):
        if start == len(word):
            return True

        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[start]:
            return False

        board[x][y], tmp = '*', board[x][y]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = any(self.dfs(board, x + dx, y + dy, word, start+1) for dx, dy in directions)
        board[x][y] = tmp
        return result