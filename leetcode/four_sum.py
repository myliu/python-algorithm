from itertools import combinations
from collections import defaultdict

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()

        two_sum = defaultdict(list)
        for (i1, n1), (i2, n2) in combinations(enumerate(nums), 2):
            # Set is used because we will test disjoint and perform set union later.
            two_sum[n1+n2] += {i1, i2},

        for t in two_sum.keys():
            if not two_sum[target-t]:
                continue

            for pair1 in two_sum[t]:
                for pair2 in two_sum[target-t]:
                    if pair1.isdisjoint(pair2):
                        res.add(tuple(sorted(nums[i] for i in pair1|pair2)))

        return list(map(list, res))

if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    print s.fourSum(nums, 0)