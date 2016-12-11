# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Reverse the linked list till the middle point
        prev = None
        curr = fast = head

        while fast and fast.next:
            fast = fast.next.next

            _next = curr.next
            curr.next = prev
            prev, curr = curr, _next

        # When the number of nodes is odd
        if fast:
            forward = curr.next
        # When the number of nodes is even
        else:
            forward = curr

        reverse = prev

        # From the middle point, compare the nodes in both directions
        while reverse and reverse.val == forward.val:
            forward, reverse = forward.next, reverse.next

        # This can be either `not reverse` or `not forward`
        return not reverse