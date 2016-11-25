# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, tmp):
            if not root:
                return 0

            curr = tmp + str(root.val)

            if not root.left and not root.right:
                return int(curr)

            return dfs(root.left, curr) + dfs(root.right, curr)

        return dfs(root, '')