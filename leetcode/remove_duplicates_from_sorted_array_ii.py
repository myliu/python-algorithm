class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        end, count = 0, 0
        for num in nums[1:]:
            if num != nums[end]:
                nums[end+1] = num
                end += 1
                count = 0
            else:
                if count == 0:
                    nums[end+1] = num
                    end += 1
                count += 1
        return end + 1

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,1,1,1,3,3])