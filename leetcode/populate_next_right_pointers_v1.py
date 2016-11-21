# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        queue = []

        if root:
            queue.append(root)

        while queue:
            current_queue = []
            next_queue = []
            for node in queue:
                current_queue.append(node)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            for i in xrange(len(current_queue)-1):
                current_queue[i].next = current_queue[i+1]
            queue = next_queue