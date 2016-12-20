class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def first(lo, hi, check):
            while lo < hi:
                mid = (lo + hi) / 2
                if check(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        # To find the first black
        top    = first(0, x,             lambda k: '1' in image[k])
        # To find the first white
        bottom = first(x, len(image),    lambda k: '1' not in image[k])
        left   = first(0, y,             lambda k: any(row[k] == '1' for row in image))
        right  = first(y, len(image[0]), lambda k: all(row[k] == '0' for row in image))
        return (bottom - top) * (right - left)

"""
["0010",
 "0110",
 "0100"]

top = 0
bottom = 3
left = 1
right = 3
"""