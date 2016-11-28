class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        result = _min = _max = nums[0]
        for num in nums[1:]:
            if num < 0:
                _min, _max = _max, _min

            _min = min(_min * num, num)
            _max = max(_max * num, num)
            result = max(result, _max)
        return result