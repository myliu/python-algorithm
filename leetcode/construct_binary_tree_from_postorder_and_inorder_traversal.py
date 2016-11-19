# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(post_end, in_start, in_end, inorder, postorder):
            if post_end < 0 or in_start > in_end:
                return None

            val = postorder[post_end]
            i = inorder.index(val)
            root = TreeNode(val)
            root.left = helper(post_end-1-(in_end-i), in_start, i-1, inorder, postorder)
            root.right = helper(post_end-1, i+1, in_end, inorder, postorder)
            return root

        return helper(len(postorder)-1, 0, len(inorder)-1, inorder, postorder)