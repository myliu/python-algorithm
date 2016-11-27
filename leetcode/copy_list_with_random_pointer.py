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
        def dfs(head, graph):
            if not head:
                return None

            if head.label in graph:
                return graph[head.label]

            clone = RandomListNode(head.label)
            graph[clone.label] = clone
            clone.next = dfs(head.next, graph)
            clone.random = dfs(head.random, graph)
            return clone

        return dfs(head, {})