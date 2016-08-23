class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = 0
        num_set = set(nums)
        for num in nums:
            if (num-1) not in num_set:
                count, tmp = 1, num+1
                while tmp in num_set:
                    tmp += 1
                    count += 1
                best = max(best, count)
        return best