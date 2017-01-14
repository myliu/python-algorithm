class BinaryTreeToDoublyLinkedList(object):

    def flatten(root):
        prev = None

        def helper(node):
            if not node:
                return None

            leftmost = helper(node.left) or node
            node.left = prev
            if prev:
                prev.right = node
            prev = node
            helper(node.right)
            return leftmost

        return helper(root)