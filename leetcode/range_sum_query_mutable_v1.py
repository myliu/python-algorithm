class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        self.tree = nums + nums
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        tree = self.tree
        i += self.n
        tree[i] = val
        while i > 0:
            left = right = i
            if i % 2 == 1:
                left -= 1
            else:
                right += 1
            tree[i/2] = tree[left] + tree[right]
            i /= 2


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        n = self.n
        tree = self.tree
        
        i += n
        j += n
        range_sum = 0
        while i <= j:
            if i % 2 == 1:
                range_sum += tree[i]
                i += 1
            if j % 2 == 0:
                range_sum += tree[j]
                j -= 1
            i /= 2
            j /= 2
        return range_sum


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)