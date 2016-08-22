class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k = rowIndex
        if k == 0:
            return [1]

        if k == 1:
            return [1, 1]

        res = [1, 1]
        for i in range(2, k+1):
            for j in range(i-1, 0, -1):
                res[j] = res[j] + res[j-1]
            res.append(1)
        return res