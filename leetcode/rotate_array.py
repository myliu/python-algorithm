class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        while k > 0:
            nums.insert(0, nums[-1])
            nums.pop(-1)
            k -= 1

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    s.rotate(nums, 1)
    for num in nums:
        print num