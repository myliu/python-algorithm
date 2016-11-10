class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        if not matrix:
            return result

        row_begin, row_end, col_begin, col_end = 0, len(matrix)-1, 0, len(matrix[0])-1

        while row_begin <= row_end and col_begin <= col_end:
            for i in range(col_begin, col_end+1):
                result += matrix[row_begin][i],
            row_begin += 1

            for i in range(row_begin, row_end+1):
                result += matrix[i][col_end],
            col_end -= 1

            if row_begin <= row_end:
                for i in range(col_end, col_begin-1, -1):
                    result += matrix[row_end][i],
                row_end -= 1

            # Example: [[1, 2], [3, 4]]
            if col_begin <= col_end:
                for i in range(row_end, row_begin-1, -1):
                    result += matrix[i][col_begin],
                col_begin += 1

        return result