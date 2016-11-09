class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def validate(queens, x, y):
            for i in range(n):
                # No need to validate any column that equals to or greater than the current column
                for j in range(y):
                    if queens[i][j] == 'Q' and (i == x or i + j == x + y or i - j == x - y):
                        return False
            return True   

        # Invariant: All columns before col should satisfy the N-Queens rule.
        def dfs(queens, col, result):
            if col == n:
                result += [''.join(row) for row in queens],
                return

            # Iterate over the rows, and try to place 'Q' on each row.
            for row in range(n):
                if validate(queens, row, col):
                    queens[row][col] = 'Q'
                    dfs(queens, col+1, result)
                    queens[row][col] = '.'


        queens = [['.'] * n for _ in range(n)]
        result = []
        dfs(queens, 0, result)
        return result