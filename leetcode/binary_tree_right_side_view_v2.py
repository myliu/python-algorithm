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
        if not root:
            return []

        queue = deque()
        queue += root,
        result = []
        while queue:
            size = len(queue)
            curr = None
            for _ in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue += curr.left,
                if curr.right:
                    queue += curr.right,
            result += curr.val,
        return result