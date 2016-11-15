class Solution(object):

    # https://discuss.leetcode.com/topic/6650/share-my-dp-solution
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        row_length, column_length = len(matrix), len(matrix[0])
        left, right, height = [0] * column_length, [column_length] * column_length, [0] * column_length
        maximal = 0
        for i in range(row_length):
            cur_left, cur_right = 0, column_length

            for j in range(column_length):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(column_length):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    cur_left = j + 1
                    left[j] = 0

            for j in range(column_length-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    cur_right = j
                    right[j] = column_length

            for j in range(column_length):
                maximal = max(maximal, (right[j] - left[j]) * height[j])

        return maximal