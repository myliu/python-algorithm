class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def validate(queens, x, y):
            for i in xrange(n):
                # No need to validate any column that equals to or greater than the current column
                for j in xrange(y):
                    if queens[i][j] == 'Q' and (i == x or i + j == x + y or i - j == x - y):
                        return False
            return True   

        def dfs(queens, col, result):
            if col == n:
                result.append(transform(queens))
                return

            # Iterate over the rows
            for i in xrange(n):
                if validate(queens, i, col):
                    queens[i][col] = 'Q'
                    dfs(queens, col+1, result)
                    queens[i][col] = '.'

        def transform(queens):
            return [''.join(row) for row in queens]

        queens = [['.' for i in xrange(n)] for j in xrange(n)]
        result = []
        dfs(queens, 0, result)
        return result