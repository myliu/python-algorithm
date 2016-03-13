class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False

        row = len(matrix)
        col = len(matrix[0])

        low, high = 0, row * col - 1

        while low <= high:
            mid = low + (high - low) / 2
            num = matrix[mid/col][mid%col]
            
            if target == num:
                return True
            elif target > num:
                low = mid + 1
            else:
                high = mid - 1

        return False