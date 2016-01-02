class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        min_dict = [[0 for i in xrange(len(row))] for row in triangle]

        def dfs(x, y):
            if x == len(triangle):
                return 0

            if min_dict[x][y] != 0:
                return min_dict[x][y]

            min_dict[x][y] = min(dfs(x+1, y), dfs(x+1, y+1)) + triangle[x][y]
            return min_dict[x][y]

        return dfs(0, 0)

if __name__ == '__main__':
    s = Solution()
    triangle = [
                    [2],
                   [3,4],
                  [6,5,7],
                 [4,1,8,3]
               ]
    print s.minimumTotal(triangle)