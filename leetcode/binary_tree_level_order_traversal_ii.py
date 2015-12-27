import collections

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = []
        q.append(root)
        stack = []
        while q:
            current_level = []
            next_level = []
            for node in q:
                current_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            stack.append(current_level)
            q = next_level

        result = []
        while stack:
            result.append(stack.pop())
        return result

if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)

    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5

    s = Solution()

    result = s.levelOrderBottom(t1)
    print result

