# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root:
                vals.append('#')
                return
            vals.append(str(root.val))
            helper(root.left)
            helper(root.right)

        vals = []
        helper(root)
        return ' '.join(vals)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper():
            s = next(vals)
            if s == '#':
                return None
            root = TreeNode(int(s))
            root.left = helper()
            root.right = helper()
            return root

        vals = iter(data.split())
        return helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))