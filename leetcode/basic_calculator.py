class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, sign, i = 0, 1, 0
        stack = []
        while i < len(s):
            if s[i].isdigit():
                _sum = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    _sum = _sum * 10 + int(s[i+1])
                    i += 1
                result += sign * _sum
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack += result,
                stack += sign,
                result, sign = 0, 1
            elif s[i] == ')':
                operator = stack.pop()
                operand = stack.pop()
                result = operand + operator * result
            i += 1
        return result