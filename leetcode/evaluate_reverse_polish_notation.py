class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack += int(token),
                continue

            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1+operand2)
            elif token == '-':
                stack.append(operand1-operand2)
            elif token == '*':
                stack.append(operand1*operand2)
            elif token == '/':
                stack.append(int(operand1*1.0/operand2))
        return stack.pop()