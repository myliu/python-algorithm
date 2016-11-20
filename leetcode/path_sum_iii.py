# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(root, sum):
            if not root:
                return 0

            count = 0
            if sum == root.val:
                count += 1

            count += dfs(root.left, sum-root.val)
            count += dfs(root.right, sum-root.val)
            return count

        if not root:
            return 0
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)