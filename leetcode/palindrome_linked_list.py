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
        current = fast = head

        while fast and fast.next:
            fast = fast.next.next

            next = current.next
            current.next = prev
            prev = current
            current = next

        # When the number of nodes is odd
        if fast:
            forward = current.next
        # When the number of nodes is even
        else:
            forward = current

        reverse = prev

        # From the middle point, compare the nodes in both directions
        while reverse and reverse.val == forward.val:
            reverse = reverse.next
            forward = forward.next

        return not reverse