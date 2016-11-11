class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1

        while lo <= hi:
            mid = (lo + hi) / 2
            num = matrix[mid/n][mid%n]
            if target == num:
                return True
            elif target > num:
                lo = mid + 1
            else:
                hi = mid - 1

        return False