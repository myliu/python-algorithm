class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def is_valid(board, i, j, c):
            for row in xrange(0, 9):
                if board[row][j] == c:
                    return False

            for col in xrange(0, 9):
                if board[i][col] == c:
                    return False

            for row in xrange(0, 3):
                for col in xrange(0, 3):
                    if board[(i/3)*3+row][(j/3)*3+col] == c:
                        return False

            return True

        def solve(board):
            if not board:
                return

            for i in xrange(len(board)):
                for j in xrange(len(board[0])):
                    c = board[i][j]
                    if c == '.':
                        for d in xrange(1, 10):
                            if is_valid(board, i, j, str(d)):
                                board[i][j] = str(d)
                                if solve(board):
                                    return True
                                board[i][j] = '.'
                        return False
            # When the entire board is filled in, return True
            return True

        solve(board)