class Solution(object):

    # https://discuss.leetcode.com/topic/5056/any-shorter-o-1-space-solution
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        col0 = 1

        for i in range(m):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0