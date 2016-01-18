class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums: 
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int 
        :type j: int
        :rtype: int 
        """
        return self.accu[j + 1] - self.accu[i]

# Your NumArray object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    print numArray.sumRange(0, 1)
    print numArray.sumRange(1, 2)