import bisect

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seq = [float('inf')] * 2
        for num in nums:
            i = bisect.bisect_left(seq, num)
            if i >= 2:
                return True
            seq[i] = num
        return False