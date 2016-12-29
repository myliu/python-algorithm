class Solution(object):

    # https://discuss.leetcode.com/topic/35976/7-lines-easy-java-solution
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        tokens = preorder.split(',')
        degree = 1
        for token in tokens:
            degree -= 1
            if degree < 0:
                return False
            if token != '#':
                degree += 2
        return degree == 0