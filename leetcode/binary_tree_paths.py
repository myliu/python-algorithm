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
        def dfs(root, tmp, results):
            if not root:
                return

            if not root.left and not root.right:
                current = '->'.join(map(str, tmp+[root.val]))
                results.append(current)
                return
            
            dfs(root.left, tmp+[root.val], results)
            dfs(root.right, tmp+[root.val], results)

        results = []
        dfs(root, [], results)
        return results