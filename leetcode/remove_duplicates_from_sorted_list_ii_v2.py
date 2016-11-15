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
        slow = dummy = ListNode(-1)
        fast = head
        slow.next = head
        while fast:
            # Find the last element in the duplicates
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            
            # Remove duplicates
            if slow.next != fast:
                slow.next = fast.next
                fast = slow.next
            # Move forward by one
            else:
                slow = slow.next
                fast = fast.next
        return dummy.next