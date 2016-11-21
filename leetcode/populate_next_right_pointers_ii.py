# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy = curr = TreeLinkNode(0)
        while root:
            if root.left:
                curr.next = root.left
                curr = curr.next
            if root.right:
                curr.next = root.right
                curr = curr.next
            root = root.next
            if not root:
                curr = dummy
                root = dummy.next
                dummy.next = None