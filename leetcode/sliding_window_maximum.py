import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque()
        out = []

        for i, n in enumerate(nums):
            # Pop all elements that are smaller than the newest element 'n'
            # This will ensure the d[0] will always be the largest element in the deque
            while d and nums[d[-1]] < n:
                d.pop()

            d += i,

            # The deque will hold a max of k elements, so we should remove the first element when the limit is hit
            if d[0] == i - k:
                d.popleft()

            # Start adding to the output list as soon as the window size is satisfied
            if i >= k - 1:
                out += nums[d[0]],

        return out