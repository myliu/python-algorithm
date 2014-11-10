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
    def levelOrder(self, root):
        result = []

        if root == None:
            return result

        q = collections.deque()
        q.append(root)

        while len(q) != 0:
            li = []
            size = len(q)

            for i in range(size):
                node = q.popleft()
                li.append(node.val)

                if node.left != None:
                    q.append(node.left)

                if node.right != None:
                    q.append(node.right)

            result.append(li)

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

    result = s.levelOrder(t1)
    print result

