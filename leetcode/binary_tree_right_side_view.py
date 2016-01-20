# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []
        queue = []
        
        if root:
            queue.append(root)

        while queue:
            out.append(queue[-1].val)
            temp_queue = []
            for node in queue:
                if node.left:
                    temp_queue.append(node.left)
                if node.right:
                    temp_queue.append(node.right)
            queue = temp_queue
        return out