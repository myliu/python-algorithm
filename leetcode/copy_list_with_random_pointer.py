# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        def dfs(head, list_dict):
            if not head:
                return None

            if head.label in list_dict:
                return list_dict[head.label]

            clone = RandomListNode(head.label)
            list_dict[head.label] = clone
            clone.next = dfs(head.next, list_dict)
            clone.random = dfs(head.random, list_dict)
            return clone

        return dfs(head, {})