# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k < 2:
            return head

        ret = head
        for i in range(k-1):
            ret = ret.next
            if not ret:
                return head

        prev = None
        current = head
        for i in range(k):
            _next = current.next
            current.next = prev
            prev = current
            current = _next

        head.next = self.reverseKGroup(current, k)

        return ret