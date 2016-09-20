class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        needed = [0] + [amount+1]*amount
        for c in coins:
            for i in range(c, amount+1):
                needed[i] = min(needed[i], needed[i-c]+1)
        return needed[-1] if needed[-1] <= amount else -1