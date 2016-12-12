import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglies = [1]
        def generate(prime):
            for ugly in uglies:
                yield ugly * prime
        pq = heapq.merge(*map(generate, [2, 3, 5]))
        while len(uglies) < n:
            ugly = next(pq)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]