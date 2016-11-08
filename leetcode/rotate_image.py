class Solution(object):
    """
     * Clockwise rotate
     * First reverse up to down, then swap the symmetry 
     * 1 2 3     7 8 9     7 4 1
     * 4 5 6  => 4 5 6  => 8 5 2
     * 7 8 9     1 2 3     9 6 3
     *
     * 1  2  3  4        13 14 15 16        13 9  5  1
     * 5  6  7  8   =>   9  10 11 12   =>   14 10 6  2
     * 9  10 11 12       5  6  7  8         15 11 7  3
     * 13 14 15 16       1  2  3  4         16 12 8  4
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Flip the matrix upside down
        for i in range(n/2):
           matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        # Flip the matrix across the diagonal
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]