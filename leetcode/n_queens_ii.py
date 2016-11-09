class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def validate(row, col):
            if (row in rows) or (row+col in sum_diagonal) or (row-col in subtract_diagonal):
                return False
            return True

        def dfs(col, count):
            for row in range(n):
                if not validate(row, col):
                    continue
                if col == n - 1:
                    count += 1
                else:
                    rows.add(row)
                    sum_diagonal.add(row+col)
                    subtract_diagonal.add(row-col)
                    count = dfs(col+1, count)
                    rows.remove(row)
                    sum_diagonal.remove(row+col)
                    subtract_diagonal.remove(row-col)
            return count


        rows = set()
        sum_diagonal = set()
        subtract_diagonal = set()
        return dfs(0, 0)