import itertools, collections

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()

        two_sum = collections.defaultdict(list)
        for (i1, n1), (i2, n2) in itertools.combinations(enumerate(nums), 2):
            two_sum[n1+n2].append({i1, i2})

        for t in two_sum.keys():
            if not two_sum[target-t]:
                continue

            for pair1 in two_sum[t]:
                for pair2 in two_sum[target-t]:
                    if pair1.isdisjoint(pair2):
                        res.add(tuple(sorted((nums[i] for i in pair1|pair2))))

        return list(map(list, res))