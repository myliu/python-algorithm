class Solution(object):

    # https://discuss.leetcode.com/topic/1344/share-some-of-my-ideas
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost or sum(gas) < sum(cost):
            return -1

        start, balance = 0, 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                start, balance = i+1, 0
        return start