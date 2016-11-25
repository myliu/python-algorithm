from collections import Counter

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def union(node1, node2):
            nodes[find(node1)] = find(node2)

        def find(node):
            if node != nodes[node]:
                nodes[node] = find(nodes[node])
            return nodes[node]

        nodes = {}
        for num in nums:
            nodes[num] = num

        for num in nums:
            if num + 1 in nodes:
                union(num, num+1)
            elif num - 1 in nodes:
                union(num-1, num)

        map(find, nodes.keys())

        return Counter(nodes.values()).most_common(1)[0][1]