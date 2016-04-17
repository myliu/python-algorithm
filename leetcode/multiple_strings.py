class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = map(int, num1)[::-1]
        l2 = map(int, num2)[::-1]
        sum = 0
        for i, m in enumerate(l1):
            for j, n in enumerate(l2):
                sum += m * n * 10 ** (i + j)
        return str(sum)