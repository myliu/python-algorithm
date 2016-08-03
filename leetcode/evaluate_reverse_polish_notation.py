class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(0 - stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())            
            elif token == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(float(op1) / op2))
            else:
                stack.append(int(token))
        return stack.pop()