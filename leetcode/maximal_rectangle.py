class Solution(object):

    # https://discuss.leetcode.com/topic/6650/share-my-dp-solution
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        height = [0] * n
        left = [0] * n
        right = [n] * n
        _max = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            curr_left = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curr_left)
                else:
                    curr_left = j + 1
                    left[j] = 0

            curr_right = n
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curr_right)
                else:
                    curr_right = j
                    right[j] = n

            for j in range(n):
                _max = max(_max, height[j] * (right[j] - left[j]))

        return _max