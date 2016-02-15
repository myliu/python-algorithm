# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, less_than=float('inf'), greater_than=float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if root.val <= greater_than or root.val >= less_than:
            return False

        return self.isValidBST(root.left, min(less_than, root.val), greater_than) and \
               self.isValidBST(root.right, less_than, max(greater_than, root.val))