# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if left_depth == right_depth:
            return 2**left_depth + self.countNodes(root.right)
        else:
            return 2**right_depth + self.countNodes(root.left)

    def depth(self, root):
        if not root:
            return 0

        return 1 + self.depth(root.left)