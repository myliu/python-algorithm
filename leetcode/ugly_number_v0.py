import heapq

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        uglies = [1]
        def generate(prime):
            for ugly in uglies:
                yield ugly * prime
        pq = heapq.merge(*map(generate, [2, 3, 5]))
        while uglies[-1] <= num:
            if uglies[-1] == num:
                return True
            ugly = next(pq)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return False