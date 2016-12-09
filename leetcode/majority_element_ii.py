class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1, candidate2, count1, count2 = 0, 1, 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            else:
                if not count1:
                    candidate1, count1 = num, 1
                elif not count2:
                    candidate2, count2 = num, 1
                else:
                    count1 -= 1
                    count2 -= 1
        return [c for c in (candidate1, candidate2) if nums.count(c) > len(nums)/3]