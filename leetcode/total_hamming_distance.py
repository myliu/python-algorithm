class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [[0,0] for _ in range(32)]
        for num in nums:
            for i in range(32):
                bits[i][num%2] += 1
                num >>= 1

        return sum(x*y for x, y in bits)