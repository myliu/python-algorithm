class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, sign = 0, '+'
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if s[i] in ('+', '-', '*', '/') or i == len(s) - 1:
                if sign == '+':
                    stack += num,
                elif sign == '-':
                    stack += -num,
                elif sign == '*':
                    stack += stack.pop() * num,
                elif sign == '/':
                    # Cast to float is to handle the negative division case:
                    # e.g., -3/2 = -2 and -3.0/2 = -1
                    stack += int(float(stack.pop()) / num),
                num, sign = 0, s[i]
        return sum(stack)