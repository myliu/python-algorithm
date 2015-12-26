class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) <= 2:
            return len(nums)

        # Keep track of current position
        j = 0
        numDuplicates = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j = j + 1
                nums[j] = nums[i]
                numDuplicates = 0
            else:
                if numDuplicates == 0:
                    j = j + 1
                    nums[j] = nums[i]
                numDuplicates = numDuplicates + 1
        return j + 1

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,1,1,1,3,3])