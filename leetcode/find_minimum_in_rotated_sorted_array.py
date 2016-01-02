class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(l, r):
            if l == r:
                return nums[l]
            mid = l + (r-l)/2
            if nums[mid] > nums[r]:
                return helper(mid+1, r)
            else:
                return helper(l, mid)

        return helper(0, len(nums)-1)

if __name__ == '__main__':
    s = Solution()
    print s.findMin([3, 1, 2])

