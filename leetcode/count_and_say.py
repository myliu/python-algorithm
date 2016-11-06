class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1):
            first, count, tmp = s[0], 0, ''
            for c in s:
                if c == first:
                    count += 1
                else:
                    tmp += str(count) + first
                    first = c
                    count = 1
            tmp += str(count) + first
            s = tmp
        return s