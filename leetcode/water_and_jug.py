class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(a, b):
            return a if b == 0 else gcd(b, a%b)

        # Deal with the case where either x or y is zero and the other one is the same as z
        if x == z or y == z or z == 0:
            return True

        # z > x + y is a case where we need to tailer the code for this particular problem
        # After all, we only have two jugs
        if x == 0 or y == 0 or z > x+y or z % gcd(x, y) != 0:
            return False

        return True