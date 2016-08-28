import math

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not nums or n < 2:
            return 0

        minimum, maximum = min(nums), max(nums)
        gap = int(math.ceil(float(maximum-minimum)/(n-1)))
        min_bucket = [float('+inf')] * (n-1)
        max_bucket = [float('-inf')] * (n-1)

        for i in nums:
            if i == minimum or i == maximum:
                continue
            index = int((i-minimum)/gap)
            min_bucket[index] = min(min_bucket[index], i)
            max_bucket[index] = max(max_bucket[index], i)

        previous, max_gap = minimum, 0
        for i in range(n-1):
            if min_bucket[i] == float('inf') and max_bucket[i] == float('-inf'):
                continue
            current_gap = min_bucket[i]-previous
            max_gap = max(max_gap, current_gap)
            previous = max_bucket[i]
        return max(max_gap, (maximum-previous))