class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.bit = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.init(i, j, matrix[i][j])

    def init(self, row, col, val):
        matrix = self.matrix
        m, n = len(matrix), len(matrix[0])
        i = row + 1
        while i <= m:
            j = col + 1
            while j <= n:
                self.bit[i][j] += val
                j += j & (-j)
            i += i & (-i)

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        matrix = self.matrix
        m, n = len(matrix), len(matrix[0])
        delta = val - matrix[row][col]
        matrix[row][col] = val
        self.init(row, col, delta)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        get_sum = self.get_sum
        return get_sum(row2+1, col2+1) - get_sum(row2+1, col1) - get_sum(row1, col2+1) + get_sum(row1, col1)

    def get_sum(self, row, col):
        result = 0
        i, j = row, col
        while i > 0:
            j = col
            while j > 0:
                result += self.bit[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return result

if __name__ == '__main__':
    matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    numMatrix = NumMatrix(matrix)
    print numMatrix.sumRegion(0, 1, 2, 3)
    numMatrix.update(1, 1, 10)
    print numMatrix.sumRegion(1, 2, 3, 4)