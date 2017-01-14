class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        cols = zip(*B)

        result = []
        for row in A:
            curr = []
            for col in cols:
                curr += sum(x * y for x, y in zip(row, col)),
            result += curr,
        return result