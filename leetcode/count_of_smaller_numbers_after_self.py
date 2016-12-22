class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1-based
        def _update(i, val):
            while i < len(bit):
                bit[i] += val
                i += i & (-i)

        # 1-based    
        def _sum(i):
            result = 0
            while i > 0:
                result += bit[i]
                i -= i & (-i)
            return result

        n = len(nums)
        # How many numbers are equal to or smaller than the index (1-based)
        bit = [0] * (n+1)
        ranks = {num: i+1 for i, num in enumerate(sorted(set(nums)))}

        counts = []
        for i in range(n-1, -1, -1):
            num = nums[i]
            rank = ranks[num]
            counts += _sum(rank-1),
            _update(rank, 1)
        return counts[::-1]