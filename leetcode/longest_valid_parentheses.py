class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        _max = count = 0
        for i, c in enumerate(s):
            if c == '(':
                stack += i,
            else:
                if stack:
                    stack.pop()
                    count += 2
                    if not stack:
                        _max = max(_max, count)
                    else:
                        # Handle the case: '()(()'
                        _max = max(_max, i-stack[-1])
                else:
                    count = 0
        return _max