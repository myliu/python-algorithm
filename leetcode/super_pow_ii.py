class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        result = 1
        # e.g., a^5347 = (a^534)^10 * a^7
        for i in b:
            result = pow(result, 10, 1337) * pow(a, i, 1337) % 1337
        return result