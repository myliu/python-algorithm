import math

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not nums or len(nums) < 2:
            return 0

        _min, _max = min(nums), max(nums)
        gap = int(math.ceil(float(_max-_min)/(n-1)))
        min_bucket = [float('inf')] * (n-1)
        max_bucket = [float('-inf')] * (n-1)

        for num in nums:
            if num == _max:
                continue
            i = (num-_min)/gap
            min_bucket[i] = min(min_bucket[i], num)
            max_bucket[i] = max(max_bucket[i], num)

        prev, max_gap = _min, 0
        for i in range(n-1):
            if min_bucket[i] == float('inf') and max_bucket[i] == float('-inf'):
                continue
            curr_gap = min_bucket[i] - prev
            max_gap = max(max_gap, curr_gap)
            prev = max_bucket[i]
        return max(max_gap, _max-prev)