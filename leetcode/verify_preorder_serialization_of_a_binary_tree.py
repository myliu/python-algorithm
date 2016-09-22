class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        tokens = preorder.split(',')
        # Compensate for root, which has no in-degree
        degree = -1
        for token in tokens:
            degree += 1
            if degree > 0:
                return False
            if token != '#':
                degree -= 2
        return degree == 0