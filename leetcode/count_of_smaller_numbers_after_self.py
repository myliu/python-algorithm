class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        bit = [0] * (n+1)
        rank = {v: i+1 for i, v in enumerate(sorted(nums))}
        res = []

        def update(i, val):
            while i < n:
                bit[i] += val
                i += i & -i

        def sum(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        for i in reversed(nums):
            res.append(sum(rank[i]-1))
            update(rank[i], 1)

        return res[::-1]