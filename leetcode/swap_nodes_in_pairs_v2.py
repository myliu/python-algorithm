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
        return self.reverse(head, 2)

    # Reuse function in Reverse Nodes in K Group
    def reverse(self, head, k):
        curr = head
        for i in range(k):
            if not curr:
                return head
            curr = curr.next

        prev, curr = None, head
        for i in range(k):
            _next = curr.next
            curr.next = prev
            prev, curr = curr, _next

        head.next = self.reverse(curr, k)

        return prev