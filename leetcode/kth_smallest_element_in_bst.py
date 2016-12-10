# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    count = 0
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        
        result = self.kthSmallest(root.left, k)
        # This line cannot be replaced with `if result` because it is possible result == 0
        if result != None:
            return result
        
        self.count += 1
        if self.count == k:
            return root.val
        
        result = self.kthSmallest(root.right, k)
        if result != None:
            return result