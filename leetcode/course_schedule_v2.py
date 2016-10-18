from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
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

        count = 0
        while queue:
            current = queue.popleft()
            count += 1
            for i in indegree[current]:
                outdegree[i] -= 1
                if not outdegree[i]:
                    queue += i,
        return count == numCourses