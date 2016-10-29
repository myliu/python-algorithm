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
            while head:
                heapq.heappush(heap, (head.val, head))
                head = head.next

        prev = dummy = ListNode(-1)
        while heap:
            _, curr = heapq.heappop(heap)
            prev.next = curr
            prev = curr

        return dummy.next