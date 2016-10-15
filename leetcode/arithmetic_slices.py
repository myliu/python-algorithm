class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 3:
            return 0

        n = len(A)
        dp = [0 for _ in range(n)]
        if A[2] - A[1] == A[1] - A[0]:
            dp[2] = 1
        for i in range(3, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)