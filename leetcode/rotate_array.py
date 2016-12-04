class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop()

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    s.rotate(nums, 1)
    for num in nums:
        print num