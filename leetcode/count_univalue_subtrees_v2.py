# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, True

            left_count, left_uni = dfs(root.left)
            right_count, right_uni = dfs(root.right)

            if not left_uni or (root.left and root.val != root.left.val):
                return left_count + right_count, False

            if not right_uni or (root.right and root.val != root.right.val):
                return left_count + right_count, False

            return left_count + right_count + 1, True

        return dfs(root)[0]