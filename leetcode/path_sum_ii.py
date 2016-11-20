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
        :rtype: List[List[int]]
        """
        def dfs(root, sum, tmp, result):
            if not root:
                return

            if not root.left and not root.right and sum - root.val == 0:
                tmp += root.val,
                result += tmp,
                return

            dfs(root.left, sum-root.val, tmp+[root.val], result)
            dfs(root.right, sum-root.val, tmp+[root.val], result)

        result = []
        dfs(root, sum, [], result)
        return result