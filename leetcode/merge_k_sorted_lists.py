import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap, res = [], []
        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next

        while heap:
            res.append(heapq.heappop(heap))

        return res