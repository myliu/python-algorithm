class Solution(object):

    # https://discuss.leetcode.com/topic/30688/readable-code-without-confusing-i-j-and-with-explanation
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1

        # nums[pivot] is the number to be swapped.
        pivot = i - 1

        if pivot != -1:
            # nums[j] is the number in the weak decreasing sequence that is just greater than pivot.
            j = len(nums) - 1
            while j > pivot:
                if nums[j] > nums[pivot]:
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break
                j -= 1

        nums[pivot+1:] = nums[pivot+1:][::-1]