# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, head))

        prev = dummy = ListNode(-1)
        while heap:
            _, curr = heapq.heappop(heap)
            _next = curr.next
            if _next:
                heapq.heappush(heap, (_next.val, _next))
            prev.next = curr
            prev = curr

        return dummy.next