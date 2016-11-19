# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def dfs(nums, left, right):
            if left > right:
                return None

            mid = left + (right-left)/2
            root = TreeNode(nums[mid])
            root.left = dfs(nums, left, mid-1)
            root.right = dfs(nums, mid+1, right)
            return root

        nums = []
        while head:
            nums += head.val,
            head = head.next
        return dfs(nums, 0, len(nums)-1)