import collections

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return max(
                    collections.Counter(
                        x
                        for i, row in enumerate(board)
                        for j, cell in enumerate(row)
                        if cell != '.'
                        for x in (('row', i, cell), ('col', j, cell,), (i/3, j/3, cell))
                    ).values() + [1]
                ) == 1