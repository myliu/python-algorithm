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
        def reverse(head):
            revtail = head
            prev = None
            while head:
                current = head
                head = head.next
                current.next = prev
                prev = current
            # return reverse head and reverse tail
            return prev, revtail

        # ohead and otail are the head and tail of the original list
        # whead and wtail are the head and tail of the window between [m, n]
        ohead = dummy = ListNode(0)
        whead = wtail = head
        # step 1
        # move wtail to the end of the window so that the distance between whead and wtail are n-m
        for i in range(n-m):
            wtail = wtail.next

        # step 2
        # shift the entire window
        dummy.next = head
        for i in range(m-1):
            ohead, whead, wtail = ohead.next, whead.next, wtail.next

        otail = wtail.next
        wtail.next = None

        # step 3
        # reverse the window
        revhead, revtail = reverse(whead)

        # step 4
        # stitch the three parts together
        ohead.next = revhead
        revtail.next = otail

        return dummy.next