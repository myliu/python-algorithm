class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        cols = []
        for col in zip(*B):
            tmp = []
            for i, num in enumerate(col):
                if num:
                    tmp += (i, num),
            cols += tmp,

        result = []
        for row in A:
            tmp = []
            for col in cols:
                _sum = 0
                for i, num in col:
                    _sum += row[i] * num
                tmp += _sum,
            result += tmp,
        return result