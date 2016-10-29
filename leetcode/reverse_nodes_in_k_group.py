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
        curr = head
        for i in range(k):
            if not curr:
                return head
            curr = curr.next

        prev, curr = None, head
        for i in range(k):
            next = curr.next
            curr.next = prev
            prev, curr = curr, next

        head.next = self.reverseKGroup(curr, k)

        return prev