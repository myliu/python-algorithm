class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for j in range(n)] for i in range(n)]
        row_begin, row_end, col_begin, col_end = 0, n-1, 0, n-1
        num = 1

        while row_begin <= row_end and col_begin <= col_end:
            for i in range(col_begin, col_end+1):
                matrix[row_begin][i] = num
                num += 1
            row_begin += 1

            for i in range(row_begin, row_end+1):
                matrix[i][col_end] = num
                num += 1
            col_end -= 1

            if row_begin <= row_end:
                for i in range(col_end, col_begin-1, -1):
                    matrix[row_end][i] = num
                    num += 1
                row_end -= 1

            if col_begin <= col_end:
                for i in range(row_end, row_begin-1, -1):
                    matrix[i][col_begin] = num
                    num += 1
                col_begin += 1

        return matrix