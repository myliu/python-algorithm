class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        i = 0  # include the house
        e = 0  # exclude the house
        for num in nums:
            # comma operator has to be used here because all the expressions 
            # to the right of the assignment operator are evaluated before
            # any of the assignments are made.
            i, e = e + num, max(i, e)
        return max(i, e)

if __name__ == '__main__':
    # Initialize Solution object
    s = Solution()

    nums = range(4)

    print nums

    print s.rob(nums)