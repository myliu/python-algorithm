class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows == 1:
            return s

        matrix = [''] * numRows
        row, step = 0, 0
        for c in s:
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            matrix[row] += c
            row += step
        return ''.join(matrix)