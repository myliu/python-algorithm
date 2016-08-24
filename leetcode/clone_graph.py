# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        def dfs(node, graph_dict):
            if not node:
                return None

            if node.label in graph_dict:
                return graph_dict[node.label]

            clone = UndirectedGraphNode(node.label)
            graph_dict[node.label] = clone
            for node in node.neighbors:
                clone.neighbors.append(dfs(node, graph_dict))
            return clone

        return dfs(node, {})