# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr, next = dummy, head, head.next

        for i in range(m-1):
            prev, curr, next = curr, next, next.next

        start, end = prev, curr
        prev, curr = curr, next

        for i in range(n-m):
            next = curr.next
            curr.next = prev
            prev, curr = curr, next

        start.next = prev
        end.next = curr

        return dummy.next