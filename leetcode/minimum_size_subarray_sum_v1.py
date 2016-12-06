class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        current_sum = i = I = J = 0
        for j, num in enumerate(nums, 1):
            current_sum += num
            if current_sum >= s:
                while i < j and current_sum - nums[i] >= s:
                    current_sum -= nums[i]
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return len(nums[I:J])

if __name__ == '__main__':
    s = Solution()
    print s.minSubArrayLen(15, [1,2,3,4,5])