class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren_dict = {')':'(', ']':'[', '>':'<', '}':'{'}
        stack = []

        for i in s:
            if i in paren_dict.values():
                stack += i,
            elif i in paren_dict.keys():
                if not stack or stack[-1] != paren_dict[i]:
                    return False
                stack.pop()

        return not stack