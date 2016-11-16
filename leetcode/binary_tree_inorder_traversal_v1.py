# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, output):
            if not root:
                return output

            helper(root.left, output)
            output.append(root.val)
            helper(root.right, output)
            return output

        output = []
        return helper(root, output)