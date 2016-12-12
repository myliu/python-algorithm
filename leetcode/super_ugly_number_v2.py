class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        size = len(primes)
        idx = [0] * size
        ugly = [1]

        for _ in range(1, n):
            _min = min(primes[i]*ugly[idx[i]] for i in range(size))
            
            for i in range(size):
                if primes[i]*ugly[idx[i]] == _min:
                    idx[i] += 1

            ugly += _min,

        return ugly[-1]