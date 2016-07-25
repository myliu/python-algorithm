class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def helper(s, tmp, result, n):
            if n == 4:
                if len(s) == 0:
                    result.append(tmp[:-1])
                return

            for k in xrange(1, 4):
                if len(s) < k:
                    continue
                val = int(s[:k])
                if val > 255 or str(val) != s[:k]:
                    continue
                helper(s[k:], tmp + s[:k] + '.', result, n+1)
        result = []
        helper(s, '', result, 0)
        return result