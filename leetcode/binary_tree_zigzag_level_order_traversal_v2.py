# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        if root == None:
            return result

        forward = True
        q = deque()
        q += root,

        while q:
            curr_level = []
            size = len(q)

            for i in range(size):
                node = q.popleft()
                curr_level += node.val,

                if node.left:
                    q += node.left,

                if node.right:
                    q += node.right,

            result += curr_level if forward else curr_level[::-1],
            forward = not forward

        return result