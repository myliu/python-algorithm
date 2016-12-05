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
        return self.helper(root)[1]

    def helper(self, node):
        if not node:
            return 0, 0

        l = self.helper(node.left)
        r = self.helper(node.right)

        # The first returned value does not include current node
        # The second returned value includes current ndoe
        return l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val)