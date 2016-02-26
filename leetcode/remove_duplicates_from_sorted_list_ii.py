# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)

        duplicated = False

        while head and head.next:
            if head.val != head.next.val:
                if not duplicated:
                    prev.next = head
                    prev = prev.next
                duplicated = False
            else:
                duplicated = True
            head = head.next
        prev.next = None if duplicated else head
        return dummy.next