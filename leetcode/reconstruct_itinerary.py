from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def visit(airport, flights, itinerary):
            # while is to handle the case such as [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
            while flights[airport]:
                visit(flights[airport].pop(), flights, itinerary)
            itinerary += airport,

        flights = defaultdict(list)
        for start, end in sorted(tickets, reverse=True):
            flights[start] += end,
        itinerary = []
        visit('JFK', flights, itinerary)
        return itinerary[::-1]