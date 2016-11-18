# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))


    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val


    def traverse(self, root):
        if not root:
            return

        self.traverse(root.left)

        if not self.first and root.val < self.prev.val:
            self.first = self.prev

        if root.val < self.prev.val:
            self.second = root

        self.prev = root

        self.traverse(root.right)