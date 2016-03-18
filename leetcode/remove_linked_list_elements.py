# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        prev.next = head
        current = head
        while current:
            next = current.next
            if current.val == val:
                current = next
                prev.next = current
            else:
                prev = current
                current = next
        return dummy.next