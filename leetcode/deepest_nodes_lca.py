# time: O(n)
# space: O(depth)

def deepest_node_lca(root):
    def helper(root):
        result, max_depth = root, 0
        for child in root.children:
            a, d = helper(child)
            if d > max_depth:
                result, max_depth = a, d
            elif d == max_depth:
                result = root
            return result, max_depth+1

    return helper(root)[0]