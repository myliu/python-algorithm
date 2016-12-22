from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = defaultdict(list)
        queue = deque()
        queue += (root, 0),

        while queue:
            node, i = queue.popleft()
            
            if not node:
                continue

            cols[i] += node.val,
            queue += (node.left, i-1),
            queue += (node.right, i+1),

        return [cols[i] for i in sorted(cols)]