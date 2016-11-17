# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node

        def trees(first, last):
            if first > last:
                return [None]

            return [node(root_val, left, right)
                    for root_val in range(first, last+1)
                    for left in trees(first, root_val-1)
                    for right in trees(root_val+1, last)]

        return trees(1, n) if n != 0 else []