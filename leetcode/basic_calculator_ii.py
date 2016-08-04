class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num, sign = 0, '+'
        for i in xrange(len(s)):
            c = s[i]

            if c.isdigit():
                num = num * 10 + int(c)

            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(float(stack.pop()) / num))
                num, sign = 0, c

        return sum(stack)