# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return 0, 0
            i1, e1 = helper(root.left)
            i2, e2 = helper(root.right)
            return root.val + e1 + e2, max(i1, e1) + max(i2, e2)
        i, e = helper(root)
        return max(i, e)