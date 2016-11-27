# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    # https://discuss.leetcode.com/topic/8570/an-easy-and-clear-way-to-sort-o-1-space
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = prev = ListNode(0)
        curr = head
        while curr:
            _next = curr.next
            # Insert between prev and prev.next
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            curr.next = prev.next
            prev.next = curr
            prev, curr = dummy, _next

        return dummy.next