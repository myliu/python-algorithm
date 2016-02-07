import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        def generate(prime):
            for ugly in uglies:
                yield ugly * prime

        # generators is a list of k generators
        generators = map(generate, primes)

        # heapq.merge merge multiple sorted inputs into a single sorted output,
        # and returns an iterator over the sorted values
        pq = heapq.merge(*generators)

        while len(uglies) < n:
            ugly = next(pq)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]

if __name__ == '__main__':
    s = Solution()
    primes = [2, 7, 13, 19]
    print s.nthSuperUglyNumber(10, primes)