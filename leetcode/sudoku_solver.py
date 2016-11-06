class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def is_valid(i, j, v):
            for row in range(9):
                if board[row][j] == v:
                    return False

            for col in range(9):
                if board[i][col] == v:
                    return False

            for m in range(3):
                for n in range(3):
                    if board[(i/3)*3+m][(j/3)*3+n] == v:
                        return False

            return True

        def solve():
            if not board:
                return False

            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in range(1, 10):
                            if is_valid(i, j, str(k)):
                                board[i][j] = str(k)
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False

            # When the entire board is filled in, return True
            return True

        solve()