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
        return self.dfs(root)[0]


    def dfs(self, root):
        if not root:
            return 0, 0
        
        global_left, local_left = self.dfs(root.left)
        global_right, local_right = self.dfs(root.right)
        
        tmp = 1
        if root.left and root.left.val == root.val + 1:
            tmp = local_left + 1
        
        if root.right and root.right.val == root.val + 1:
            tmp = max(tmp, local_right + 1)

        return max(tmp, global_left, global_right), tmp