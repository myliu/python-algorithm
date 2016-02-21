# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        ret = head.next
        if not ret:
            return head

        prev, current = None, head
        for i in range(2):
            _next = current.next
            current.next = prev
            prev = current
            current = _next

        head.next = self.swapPairs(current)

        return ret