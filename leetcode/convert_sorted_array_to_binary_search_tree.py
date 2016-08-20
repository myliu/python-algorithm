# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def dfs(nums, left, right):
            if left > right:
                return None

            if left == right:
                return TreeNode(nums[left])

            mid = left + (right-left)/2
            root = TreeNode(nums[mid])
            root.left = dfs(nums, left, mid-1)
            root.right = dfs(nums, mid+1, right)
            return root

        return dfs(nums, 0, len(nums)-1)