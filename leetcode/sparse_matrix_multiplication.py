class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        cols = [[(j, b)
                for j, b in enumerate(col) if b]
                for col in zip(*B)]
        # cols of B will map to rows of A
        return [[sum(row[j]*b for j, b in col)
                for col in cols]
                for row in A]