class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Maintain an array of unique elements.
        # end is the index of the last element of the array.
        if not nums:
            return 0

        end = 0
        for num in nums:
            if num != nums[end]:
                nums[end+1] = num
                end += 1
        return end + 1


if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1, 1, 2, 2, 2, 3])