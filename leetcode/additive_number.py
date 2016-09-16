class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def valid(a, b, start, num):
            if start == len(num):
                return True
            c = str(int(a) + int(b))
            return num[start:].startswith(c) and valid(b, c, start+len(c), num)

        n = len(num)
        for i in range(1, n/2+1):
            if num[0] == '0' and i > 1:
                return False
            a = num[:i]
            j = 1
            while max(i, j) <= n-i-j:
                if num[i] == '0' and j > 1:
                    break
                b = num[i:i+j]
                if valid(a, b, i+j, num):
                    return True
                j += 1
        return False