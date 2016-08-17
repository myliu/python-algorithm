class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tokens = path.split('/')
        stack = []
        for token in tokens:
            if token not in ('', '.', '..'):
                stack.append(token)
            elif token == '..' and stack:
                stack.pop()

        return '/' + '/'.join(stack)