class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        self.nums, self.bit = nums, [0] * (n+1)
        for i, num in enumerate(nums):
            # Convert from 0-based index (nums) to 1-based index (bit)
            self._update(i+1, num)

    # i is 1-based
    def _update(self, i, val):
        while i <= len(self.nums):
            self.bit[i] += val
            i += i & -i

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self._update(i+1, diff)

    # i is 1-based
    def _sum(self, i):
        result = 0
        while i >= 1:
            result += self.bit[i]
            i -= i & -i
        return result

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        # Convert from 0-based index (nums) to 1-based index (bit)
        i, j = i + 1, j + 1
        return self._sum(j) - self._sum(i-1)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)