class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False

        d = {stone: set() for stone in stones}
        d[1].add(1)
        for i in stones[:-1]:
            for j in d[i]:
                for k in range(j-1, j+2):
                    if k > 0 and i+k in d:
                        d[i+k].add(k)
        return bool(d[stones[-1]])