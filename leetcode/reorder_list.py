# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # Assume the input is [1, 2, 3, 4, 5, 6]
        if not head:
            return

        # Split the list into two halves
        # Post-split:
        # First half: [1, 2, 3, 4, 5, 6]
        # Seoncd half: [4, 5, 6]
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        # By assign curr.next to None, we carved out the first half
        # [1, 2, 3, 4]
        # Post-reverse:
        # Second half: [6, 5, 4]
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Merge
        # We don't need to worry about the last node since the last node in both list are the same
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next