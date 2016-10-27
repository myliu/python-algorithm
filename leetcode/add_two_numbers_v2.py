# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = prev = ListNode(-1)
        carry = 0
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + carry
                carry = 1 if val > 9 else 0
                current = ListNode(val % 10)
                l1, l2 = l1.next, l2.next
            elif l1:
                val = l1.val + carry
                carry = 1 if val > 9 else 0
                current = ListNode(val % 10)
                l1 = l1.next
            else:
                val = l2.val + carry
                carry = 1 if val > 9 else 0
                current = ListNode(val % 10)
                l2 = l2.next
            prev.next = current
            prev = current

        if carry == 1:
            current = ListNode(1)
            prev.next = current

        return head.next