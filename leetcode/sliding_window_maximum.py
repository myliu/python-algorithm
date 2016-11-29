from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        q = deque()
        result = []

        for i in range(n):
            # Pop all elements that are smaller than the newest element nums[i]
            # This will ensure the q[0] will always be the largest element in the deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q += i,

            # The deque will hold a max of k elements, so we should remove the first element when the limit is hit
            if i - q[0] == k:
                q.popleft()

            # Start adding to the result as soon as the window size is satisfied
            if i >= k - 1:
                result += nums[q[0]],

        return result