# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        left = right = dummy = ListNode(-1)
        dummy.next = head 

        for i in range(n):
            right = right.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next