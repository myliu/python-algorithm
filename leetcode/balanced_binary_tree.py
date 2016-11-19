# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    UNBALANCED = -1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.depth(root) != self.UNBALANCED

    def depth(self, root):
        if not root:
            return 0

        l = self.depth(root.left)
        r = self.depth(root.right)

        if l == self.UNBALANCED or r == self.UNBALANCED or abs(l - r) > 1:
            return self.UNBALANCED

        return max(l, r) + 1