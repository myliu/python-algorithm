# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        predecessors = []
        successors = []
        self.init_predecessors(root, target, predecessors)
        self.init_successors(root, target, successors)

        # To handle the case where target exists in BST
        if predecessors and successors and predecessors[-1] == successors[-1]:
            self.next_predecessor(predecessors)

        result = []
        for _ in range(k):
            if not predecessors:
                result += self.next_successor(successors),
            elif not successors:
                result += self.next_predecessor(predecessors),
            else:
                predecessor = predecessors[-1].val
                successor = successors[-1].val
                if abs(predecessor-target) < abs(successor-target):
                    result += self.next_predecessor(predecessors),
                else:
                    result += self.next_successor(successors),
        return result

    def init_predecessors(self, root, target, predecessors):
        while root:
            if root.val == target:
                predecessors += root,
                break
            elif root.val < target:
                predecessors += root,
                root = root.right
            else:
                root = root.left

    def init_successors(self, root, target, successors):
        while root:
            if root.val == target:
                successors += root,
                break
            elif root.val < target:
                root = root.right
            else:
                successors += root,
                root = root.left

    def next_predecessor(self, predecessors):
        curr = predecessors.pop()
        val = curr.val
        curr = curr.left
        while curr:
            predecessors += curr,
            curr = curr.right
        return val

    def next_successor(self, successors):
        curr = successors.pop()
        val = curr.val
        curr = curr.right
        while curr:
            successors += curr,
            curr = curr.left
        return val