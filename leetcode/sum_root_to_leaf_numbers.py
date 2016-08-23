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
        def dfs(root, path, sums):
            if not root:
                return sums

            current = path + str(root.val)

            if not root.left and not root.right:
                sums += int(current)
                return sums

            return sums + dfs(root.left, current, sums) + dfs(root.right, current, sums)

        return dfs(root, '', 0)