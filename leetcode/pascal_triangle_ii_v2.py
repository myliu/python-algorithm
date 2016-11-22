class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = []
        for i in range(rowIndex+1):
            row = [1] + row
            for j in range(1, len(row)-1):
                row[j] = row[j] + row[j+1]
        return row