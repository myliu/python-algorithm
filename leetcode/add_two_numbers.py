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
        def to_int(node):
            return node.val + 10 * to_int(node.next) if node else 0

        def to_list(num):
            node = ListNode(num % 10)
            if num >= 10:
                node.next = to_list(num / 10)
            return node

        return to_list(to_int(l1) + to_int(l2))