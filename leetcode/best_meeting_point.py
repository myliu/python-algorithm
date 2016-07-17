class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def find_min(person):
            length = len(person)
            i, j, result = 0, length - 1, 0
            while i < j:
                result += person[j] - person[i]
                i += 1
                j -= 1
            return result

        row, column = [], []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)
                    column.append(j)

        return find_min(sorted(row)) + find_min(sorted(column))