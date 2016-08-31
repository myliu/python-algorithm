class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        bottom = max(B, F)
        overlap = (right-left)*(top-bottom) if (right > left and top > bottom) else 0
        return (C-A)*(D-B) + (G-E)*(H-F) - overlap