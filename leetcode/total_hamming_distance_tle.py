from itertools import combinations

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for a, b in combinations(nums, 2):
            count += bin(a^b).count('1')
        return count