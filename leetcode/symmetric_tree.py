# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node1, node2):
            if node1 and node2 and node1.val == node2.val:
                return helper(node1.left, node2.right) and helper(node1.right, node2.left)
            return node1 == node2

        if not root:
            return True

        return helper(root.left, root.right)