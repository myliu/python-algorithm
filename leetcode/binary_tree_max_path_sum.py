# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.max_sum = float("-inf")


    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path_down(root)
        return self.max_sum


    def max_path_down(self, root):
        if not root:
            return 0

        left = max(0, self.max_path_down(root.left))
        right = max(0, self.max_path_down(root.right))
        self.max_sum = max(self.max_sum, left + right + root.val)
        return max(left, right) + root.val