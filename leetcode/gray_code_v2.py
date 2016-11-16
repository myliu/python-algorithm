class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        if n == 1:
            return [0, 1]

        code = self.grayCode(n-1)
        for i in range(len(code)-1, -1, -1):
            code += 2 ** (n-1) + code[i],
        return code