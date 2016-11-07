class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        lst1 = map(int, num1)[::-1]
        lst2 = map(int, num2)[::-1]
        _sum = 0
        for i, m in enumerate(lst1):
            for j, n in enumerate(lst2):
                _sum += m * n * 10 ** (i+j)
        return str(_sum)