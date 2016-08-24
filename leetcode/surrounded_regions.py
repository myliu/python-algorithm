class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 1- Turn 'O' on the border to '1'
        # 2- Turn remaining 'O' to 'X'
        # 3- Turn '1' to 'O'
        def check(board, i, j, row, col):
            if board[i][j] == 'O':
                board[i][j] = '1'
                if i - 1 > 0:
                    check(board, i-1, j, row, col)
                if j - 1 > 0:
                    check(board, i, j-1, row, col)
                if i + 1 < row - 1:
                    check(board, i+1, j, row, col)
                if j + 1 < col - 1:
                    check(board, i, j+1, row, col)

        if not board:
            return

        row, col = len(board), len(board[0])
        for i in range(row):
            check(board, i, 0, row, col)
            if col > 1:
                check(board, i, col-1, row, col)

        for j in range(1, col-1):
            check(board, 0, j, row, col)
            if row > 1:
                check(board, row-1, j, row, col)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(row):
            for j in range(col):
                if board[i][j] == '1':
                    board[i][j] = 'O'