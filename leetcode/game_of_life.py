class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                live_neighbors = self.live_neighbors(board, m, n, i, j)
                if board[i][j] == 1 and live_neighbors in (2, 3):
                    board[i][j] = 3
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


    def live_neighbors(self, board, m, n, i, j):
        count = 0
        for x in range(max(i-1, 0), min(i+1, m-1)+1):
            for y in range(max(j-1, 0), min(j+1, n-1)+1):
                count += board[x][y] & 1
        count -= board[i][j]
        return count