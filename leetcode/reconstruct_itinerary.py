import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        routes = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            routes.append(airport)
        visit('JFK')
        return routes[::-1]