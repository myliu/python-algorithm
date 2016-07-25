class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def totalNQueensHelper(col, count):
            for row in xrange(n):
                if (row in rows) or (row + col in sum_diagonal) or (row - col in subtract_diagonal):
                    continue

                if col == n - 1:
                    count += 1
                else:
                    rows.add(row)
                    sum_diagonal.add(row+col)
                    subtract_diagonal.add(row-col)
                    count = totalNQueensHelper(col+1, count)
                    rows.remove(row)
                    sum_diagonal.remove(row+col)
                    subtract_diagonal.remove(row-col)

            return count

        rows = set()
        sum_diagonal = set()
        subtract_diagonal = set()
        return totalNQueensHelper(0, 0)