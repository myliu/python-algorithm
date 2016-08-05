class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    top = stack[-1]
                    if s[top] == '(':
                        stack.pop()
                        continue
                stack.append(i)

        if not stack:
            return len(s)

        left, maxlen = -1, 0
        for i in stack:
            maxlen = max(maxlen, i-left-1)
            left = i
        maxlen = max(maxlen, len(s)-left-1) 
        return maxlen