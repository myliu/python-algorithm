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
                return 0, 0

            left_size, left_uni = dfs(root.left)
            right_size, right_uni = dfs(root.right)

            uni = left_uni + right_uni

            if left_size == left_uni and right_size == right_uni and \
                (not root.left or root.left.val == root.val) and \
                (not root.right or root.right.val == root.val):
                    uni += 1
            return 1+left_size+right_size, uni

        return dfs(root)[1]