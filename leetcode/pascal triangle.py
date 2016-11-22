class Solution(object):

    # https://discuss.leetcode.com/topic/6805/my-concise-solution-in-java
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        row = []
        for i in range(numRows):
            row = [1] + row
            for j in range(1, len(row)-1):
                row[j] = row[j] + row[j+1]
            result += row,
        return result