class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost or sum(gas) < sum(cost):
            return -1

        pos, balance = 0, 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                pos, balance = i+1, 0
        return pos