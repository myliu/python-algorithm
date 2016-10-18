from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        outdegree = defaultdict(int)
        indegree = defaultdict(list)

        for i, j in prerequisites:
            outdegree[i] += 1
            indegree[j] += i,

        queue = deque()
        for i in range(numCourses):
            if not outdegree[i]:
                queue += i,

        result = []
        while queue:
            current = queue.popleft()
            result += current,
            for i in indegree[current]:
                outdegree[i] -= 1
                if not outdegree[i]:
                    queue += i,
        return result if len(result) == numCourses else []