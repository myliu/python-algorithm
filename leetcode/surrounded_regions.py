class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def check(i, j):
            if board[i][j] == 'O':
                board[i][j] = '1'
                if i - 1 > 0:
                    check(i-1, j)
                if i + 1 < m - 1:
                    check(i+1, j)
                if j - 1 > 0:
                    check(i, j-1)
                if j + 1 < n - 1:
                    check(i, j+1)

        if not board:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            check(i, 0)
            if n > 1:
                check(i, n-1)

        for j in range(n):
            check(0, j)
            if m > 1:
                check(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if board[i][j] == '1':
                    board[i][j] = 'O'