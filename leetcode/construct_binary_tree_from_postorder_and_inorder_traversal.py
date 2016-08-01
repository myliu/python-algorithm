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
        def helper(post_start, in_start, in_end, inorder, postorder):
            if post_start < 0 or in_start > in_end:
                return None
            root = TreeNode(postorder[post_start])
            in_mid = inorder.index(postorder[post_start])
            root.left = helper(post_start-1-(in_end-in_mid), in_start, in_mid-1, inorder, postorder)
            root.right = helper(post_start-1, in_mid+1, in_end, inorder, postorder)
            return root

        return helper(len(postorder)-1, 0, len(inorder)-1, inorder, postorder)