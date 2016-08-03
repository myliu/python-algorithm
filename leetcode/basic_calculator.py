class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, sign, i = 0, 1, 0
        stack = []
        while i < len(s):
            if s[i].isdigit():
                sum = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    sum = sum * 10 + int(s[i+1])
                    i += 1
                res += sign * sum
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif s[i] == ')':
                operator = stack.pop()
                operand = stack.pop()
                res = operand + res * operator
            i += 1
        return res