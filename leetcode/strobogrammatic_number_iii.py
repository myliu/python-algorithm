class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]

        def dfs(low, high, tmp, left, right):
            if left > right:
                num = int(''.join(tmp))
                return 1 if int(low) <= num <= int(high) else 0

            count = 0
            for m, n in pairs:
                tmp[left], tmp[right] = m, n
                if len(tmp) > 1 and tmp[0] == '0' or \
                   left == right and m != n:
                       continue
                count += dfs(low, high, tmp, left+1, right-1)
            return count

        return sum(dfs(low, high, [None]*i, 0, i-1)
                   for i in range(len(low), len(high)+1))