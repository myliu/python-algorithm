# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(pre_start, in_start, in_end, preorder, inorder):
            if pre_start >= len(preorder) or in_start > in_end:
                return None

            val = preorder[pre_start]
            i = inorder.index(val)
            root = TreeNode(val)
            root.left = helper(pre_start+1, in_start, i-1, preorder, inorder)
            root.right = helper(pre_start+1+i-in_start, i+1, in_end, preorder, inorder)
            return root

        return helper(0, 0, len(inorder)-1, preorder, inorder)