class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return
        
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
        
        return triangle[0][0]