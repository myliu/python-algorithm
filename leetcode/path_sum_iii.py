# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    """
    The difference between pathSum and path_sum_from_root is that
    path_sum_from_root returns the count of paths, where each path starts from root,
    but may or may not end at leaf.
    """
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def path_sum_from_root(root, sum):
            if not root:
                return 0

            count = 0
            if sum == root.val:
                count += 1

            count += path_sum_from_root(root.left, sum-root.val)
            count += path_sum_from_root(root.right, sum-root.val)
            return count

        if not root:
            return 0
        return path_sum_from_root(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)