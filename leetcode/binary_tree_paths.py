# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def dfs(root, tmp, result):
            if not root:
                return

            if not root.left and not root.right:
                tmp += root.val,
                result += '->'.join(map(str,tmp)),
                return

            dfs(root.left, tmp+[root.val], result)
            dfs(root.right, tmp+[root.val], result)

        result = []
        dfs(root, [], result)
        return result