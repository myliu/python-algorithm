# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        current, count = head, 1
        while current.next:
            current = current.next
            count += 1

        # Make a circle
        current.next = head
        
        for i in range(count-k%count):
            current = current.next

        new_head = current.next
        current.next = None
        return new_head