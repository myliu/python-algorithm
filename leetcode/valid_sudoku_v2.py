from collections import Counter

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        comb = []
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != '.':
                    for k in (('row', i, cell), ('col', j, cell), (i/3, j/3, cell)):
                        comb += k,
        counter = Counter(comb)
        return max(counter.values()) == 1