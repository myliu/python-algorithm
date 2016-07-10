# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(curr):
            prev = None
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev

        head = curr = reverse(head)
        while curr.val == 9:
            curr.val = 0
            if not curr.next:
                curr.next = ListNode(0)
            curr = curr.next
        curr.val += 1

        return reverse(head)