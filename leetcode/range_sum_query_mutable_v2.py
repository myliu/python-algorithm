class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        self.nums = nums
        self.bit = [0] * (n+1)
        for i in range(n):
            self.init(i, nums[i])

    def init(self, i, val):
        n = len(self.nums)
        i += 1
        while i <= n:
            self.bit[i] += val
            i += (i & -i)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.init(i, diff)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.get_sum(j+1, self.bit) - self.get_sum(i, self.bit)

    def get_sum(self, i, bit):
        result = 0
        while i > 0:
            result += bit[i]
            i -= (i & -i)
        return result

if __name__ == '__main__':
    nums = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
    numArray = NumArray(nums)
    print numArray.sumRange(0, 1)
    numArray.update(1, 10)
    print numArray.sumRange(1, 2)