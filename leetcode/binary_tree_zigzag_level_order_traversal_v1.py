from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        q1, q2 = deque(), deque()
        q1.append(root)
        while q1 or q2:
            tmp = []
            while q1:
                node = q1.pop()
                tmp.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            if tmp:
                res.append(tmp)

            tmp = []
            while q2:
                node = q2.pop()
                tmp.append(node.val)
                if node.right:
                    q1.append(node.right)
                if node.left:
                    q1.append(node.left)
            if tmp:
                res.append(tmp)
        return res