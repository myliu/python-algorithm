class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        count = [0]
        pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]

        def dfs(low, high, tmp, left, right):
            if left > right:
                s = int(''.join(tmp))
                if s < int(low) or s > int(high):
                    return
                count[0] += 1
                return

            for m, n in pairs:
                tmp[left], tmp[right] = m, n
                if len(tmp) != 1 and tmp[0] == '0':
                    continue
                if (left < right) or (left == right and m == n):
                    dfs(low, high, tmp, left+1, right-1)

        for i in xrange(len(low), len(high)+1):
            dfs(low, high, [None]*i, 0, i-1)
        return count[0]