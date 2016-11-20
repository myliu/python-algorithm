# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

# https://discuss.leetcode.com/topic/64526/17-ms-o-n-java-prefix-sum-method
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # prefix_sum stores the prefix sum from root.
        # prefix_sum_count:
        #   key:   prefix_sum
        #   value: count
        def dfs(root, prefix_sum, target, prefix_sum_count):
            if not root:
                return 0

            prefix_sum += root.val
            path_sum_to_curr = prefix_sum_count[prefix_sum-target]
            prefix_sum_count[prefix_sum] += 1
            count = path_sum_to_curr + \
                    dfs(root.left, prefix_sum, target, prefix_sum_count) + \
                    dfs(root.right, prefix_sum, target, prefix_sum_count) 
            prefix_sum_count[prefix_sum] -= 1
            return count

        if not root:
            return 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        return dfs(root, 0, sum, prefix_sum_count)