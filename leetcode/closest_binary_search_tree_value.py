# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return self.helper(root, target, float('inf'))

    def helper(self, root, target, closest):
        if not root:
            return closest

        closest = root.val if abs(root.val-target) < abs(closest-target) else closest

        if target > root.val:
            return self.helper(root.right, target, closest)
        else:
            return self.helper(root.left, target, closest)