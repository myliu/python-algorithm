# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def dfs(node, graph):
            if not node:
                return None

            if node.label in graph:
                return graph[node.label]

            clone = UndirectedGraphNode(node.label)
            graph[clone.label] = clone
            for node in node.neighbors:
                clone.neighbors += dfs(node, graph),
            return clone

        return dfs(node, {})