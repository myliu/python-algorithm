import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def max_sum_subarray(nums, k):
            max_sum = float('-inf')
            prefix_sum = 0
            prefix_sums = [float('inf')]
            for num in nums:
                bisect.insort(prefix_sums, prefix_sum)
                prefix_sum += num
                i = bisect.bisect_left(prefix_sums, prefix_sum-k)
                max_sum = max(max_sum, prefix_sum-prefix_sums[i])
            return max_sum

        max_sum = float('-inf')
        columns = zip(*matrix)
        for left in range(len(columns)):
            row_sum = [0] * len(matrix)
            for column in columns[left:]:
                row_sum = map(int.__add__, column, row_sum)
                max_sum = max(max_sum, max_sum_subarray(row_sum, k))
        return max_sum