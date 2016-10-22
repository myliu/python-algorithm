class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = _max = 0
        for i in range(32)[::-1]:
            prefixes = set()
            mask |= (1 << i)
            for num in nums:
                prefixes.add(num & mask)

            tmp = _max | (1 << i)
            for prefix in prefixes:
                if (prefix ^ tmp) in prefixes:
                    _max = tmp
                    break

        return _max