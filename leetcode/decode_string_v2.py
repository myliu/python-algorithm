import re

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        # The initial element in the stack is purely to keep track of the result
        # Thus, the count can be anything, not just 0
        stack += [0, ''],
        num = ''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack += [int(num), ''],
                num = ''
            elif ch == ']':
                count, str = stack.pop()
                stack[-1][1] += count * str
            else:
                stack[-1][1] += ch
        return stack[-1][1]