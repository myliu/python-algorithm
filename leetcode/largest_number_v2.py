class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        cmp = lambda x,y: 1 if x+y > y+x else -1 if x+y < y+x else 0
        nums = map(str, nums)
        nums.sort(cmp=cmp, reverse=True)
        result = ''.join(nums).lstrip('0')
        return result if result else '0'