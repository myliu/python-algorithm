class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        n = len(A)
        sm = sum(A)
        mx = iteration = sum(a*b for a,b in zip(A, range(n)))

        for i in range(1, n):
            iteration = iteration - sm + A[i-1]*n
            mx = max(mx, iteration)
        return mx