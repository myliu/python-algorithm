# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(head2))

    def merge(self, node1, node2):
        curr = dummy = ListNode(0)

        while node1 and node2:
            if node1.val < node2.val:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            curr = curr.next

        if node1:
            curr.next = node1
        else:
            curr.next = node2

        return dummy.next