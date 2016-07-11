class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        S = {-1:set()}
        for n in sorted(nums):
            # Here's an optimization
            # We only need to compare n with the largest element in the set, which is k
            S[n] = max((S[k] for k in S if n % k == 0), key=len) | {n}
        return list(max(S.values(), key=len))