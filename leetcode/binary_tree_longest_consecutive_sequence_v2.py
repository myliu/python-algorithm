# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, parent, length):
            if not root:
                return length

            length = length + 1 if root.val - parent == 1 else 1
            return max((dfs(root.left, root.val, length), dfs(root.right, root.val, length), length))

        if not root:
            return 0
        return max(dfs(root.left, root.val, 1), dfs(root.right, root.val, 1))