# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, upper_bound=float('inf'), lower_bound=float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if root.val <= lower_bound or root.val >= upper_bound:
            return False

        return self.isValidBST(root.left, min(upper_bound, root.val), lower_bound) and \
               self.isValidBST(root.right, upper_bound, max(lower_bound, root.val))