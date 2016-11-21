# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from collections import deque

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        queue = deque()
        queue += root,

        while queue:
            size = len(queue)
            curr_level = []

            for i in range(size):
                node = queue.popleft()
                curr_level += node,
                if node.left:
                    queue += node.left,
                if node.right:
                    queue += node.right,

            for i in range(size-1):
                curr_level[i].next = curr_level[i+1]