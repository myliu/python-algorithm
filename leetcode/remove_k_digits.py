class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for ch in num:
            while k and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # `or '0'` is to handle the case where stack is empty
        # stack[:-k or None] is to handle the case where k has not reached 0
        # stack[:-k] won't work because when k is actually 0, we don't want to slice at all
        # when k is 0, we will use stack[:None], which is the same as stack
        return ''.join(stack[:-k or None]).lstrip('0') or '0'