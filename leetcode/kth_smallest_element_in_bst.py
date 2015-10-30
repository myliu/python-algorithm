# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    count = 0

    def kthSmallest(self, root, k):
        if root == None:
            return

        res = self.kthSmallest(root.left, k)
        if res != None:
            return res

        self.count = self.count + 1
        print self.count
        if self.count == k:
            return root.val

        res = self.kthSmallest(root.right, k)
        if res != None:
            return res


if __name__ == '__main__':
    t1 = TreeNode(10)
    t2 = TreeNode(5)
    t3 = TreeNode(15)
    t4 = TreeNode(12)
    t5 = TreeNode(18)

    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5

    s = Solution()

    print s.kthSmallest(t1, 7)