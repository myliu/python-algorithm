class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        row = triangle[-1][:]
        for i in range(n-2, -1, -1):
            for j, v in enumerate(triangle[i]):
                row[j] = v + min(row[j], row[j+1])
        return row[0]