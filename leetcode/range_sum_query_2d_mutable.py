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
        for i in range(1, m+1):
            for j in range(1, n+1):
                self._update(i, j, matrix[i-1][j-1])

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[row][col]
        self._update(row+1, col+1, delta)
        self.matrix[row][col] = val
        
    def _update(self, row, col, val):
        m, n = len(self.matrix), len(self.matrix[0])
        i = row
        while i <= m:
            j = col
            while j <= n:
                self.bit[i][j] += val
                j += j & (-j)
            i += i & (-i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self._sum(row2+1, col2+1) - self._sum(row1, col2+1) - self._sum(row2+1, col1) + self._sum(row1, col1)
        
    def _sum(self, row, col):
        i = row
        result = 0
        while i > 0:
            j = col
            while j > 0:
                result += self.bit[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return result

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)

if __name__ == '__main__':
    matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    numMatrix = NumMatrix(matrix)
    print numMatrix.bit
    print numMatrix.sumRegion(0, 1, 2, 3)
    numMatrix.update(1, 1, 10)
    print numMatrix.sumRegion(1, 2, 3, 4)