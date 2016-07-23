class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def dfs(visited, skip, current, remaining):
            if remaining < 0:
                return 0
            if remaining == 0:
                return 1
            visited[current] = True
            result = 0
            for i in xrange(1, 10):
                if not visited[i] and (skip[current][i] == 0 or visited[skip[current][i]]):
                    result += dfs(visited, skip, i, remaining-1)
            visited[current] = False
            return result

        visited = [False] * 10
        skip = [[0 for j in xrange(11)] for i in xrange(11)]
        skip[1][3] = skip[3][1] = 2
        skip[4][6] = skip[6][4] = 5
        skip[7][9] = skip[9][7] = 8
        skip[1][7] = skip[7][1] = 4
        skip[2][8] = skip[8][2] = 5
        skip[3][9] = skip[9][3] = 6
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = 5
        result = 0
        for i in xrange(m, n+1):
            result += dfs(visited, skip, 1, i-1) * 4 # 1, 3, 7, 9 are the same
            result += dfs(visited, skip, 2, i-1) * 4 # 2, 4, 6, 8 are the same
            result += dfs(visited, skip, 5, i-1)
        return result