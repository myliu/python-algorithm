class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def live_neighbors(board, m, n, i, j):
            lives = 0
            for x in range(max(i-1, 0), min(i+1, m-1)+1):
                for y in range(max(j-1, 0), min(j+1, n-1)+1):
                    lives += board[x][y] & 1
            lives -= board[i][j] & 1
            return lives

        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                lives = live_neighbors(board, m, n, i, j)
                if board[i][j] == 1 and lives in (2, 3):
                    board[i][j] = 3
                elif board[i][j] == 0 and lives == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1