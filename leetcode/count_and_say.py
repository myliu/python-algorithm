class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in xrange(n-1):
            current, count, temp = s[0], 0, ''
            for i in s:
                if i == current:
                    count += 1
                else:
                    temp += str(count) + current
                    current = i
                    count = 1
            s = temp + str(count) + current
        return s