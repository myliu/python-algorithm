from collections import deque

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        f = lambda x: a*x*x + b*x + c
        n = len(nums)
        i, j = 0, n-1
        res = deque()
        while i <= j:
            if a >= 0:
                if f(nums[i]) >= f(nums[j]):
                    res.appendleft(f(nums[i]))
                    i += 1
                else:
                    res.appendleft(f(nums[j]))
                    j -= 1
            else:
                if f(nums[i]) <= f(nums[j]):
                    res.append(f(nums[i]))
                    i += 1
                else:
                    res.append(f(nums[j]))
                    j -= 1
        return list(res)