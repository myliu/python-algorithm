# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        prev, prev_right = None, None
        while root:
            root.left, root.right, prev_right, prev, root = prev_right, prev, root.right, root, root.left
        return prev