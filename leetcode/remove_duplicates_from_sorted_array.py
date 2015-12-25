class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        size = 0
        for i in range(len(nums)):
            if nums[size] != nums[i]:
                size = size + 1
                nums[size] = nums[i]
        return size + 1


if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1, 1, 2, 2, 2, 3])