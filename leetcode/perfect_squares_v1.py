import collections

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = collections.deque([(0, 0)])
        visited = set()
        while q:
            i, step = q.popleft()
            step += 1
            for j in xrange(1, n+1):
                k = i + j * j
                if k == n:
                    return step
                elif k > n:
                    break;
                if k not in visited:
                    visited.add(k)
                    q.append((k, step))