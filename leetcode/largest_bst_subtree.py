# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # https://discuss.leetcode.com/topic/36966/short-python-solution
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, 0, float('inf'), float('-inf')
            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)
            n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
            return max(N1, n, N2), n, min(min1, root.val), max(max2, root.val)
        return dfs(root)[0]