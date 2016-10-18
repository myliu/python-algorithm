from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree = [[] for _ in xrange(numCourses)]
        out_degree = [0] * numCourses

        for i, j in prerequisites:
            in_degree[j].append(i)
            out_degree[i] += 1

        dq = collections.deque()
        for course, degree in enumerate(out_degree):
            if degree == 0:
                dq.append(course)

        k = 0
        while dq:
            k += 1
            i = dq.popleft()
            for j in in_degree[i]:
                out_degree[j] -= 1
                if out_degree[j] == 0:
                    dq.append(j)

        return k == numCourses