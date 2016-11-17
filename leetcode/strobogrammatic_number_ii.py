class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Pass n as number cannot start with 0.
        # We need to detect the top level of the recursion.
        def dfs(m, n):
            if m == 0:
                return ['']

            if m == 1:
                return ['0', '1', '8']

            prev = dfs(m-2, n)
            curr = []

            for p in prev:
                if m != n:
                    curr += '0' + p + '0',
                curr += '1' + p + '1',
                curr += '6' + p + '9',
                curr += '8' + p + '8',
                curr += '9' + p + '6',

            return curr

        return dfs(n, n)