class Solution(object):

    def minCost(self, costs):
        return min(reduce(lambda (A,B,C), (a,b,c): (a+min(B,C), b+min(A,C), c+min(A,B)), costs, [0]*3))