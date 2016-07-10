import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def order(root, dic):
            """
            Function order returns the level of current node (namely, root)
            e.g., the level of the leaf node is 1
            As a side effect of the function, the value of current node is inserted to the dictionary
            """
            if not root:
                return 0
            left_level = order(root.left, dic)
            right_level = order(root.right, dic)
            current_level = max(left_level, right_level) + 1
            dic[current_level].append(root.val)
            return current_level

        # dic
        # key: level
        # value: list of node values
        dic, ret = collections.defaultdict(list), []
        order(root, dic)
        for i in range(1, len(dic) + 1):
            ret.append(dic[i])
        return ret