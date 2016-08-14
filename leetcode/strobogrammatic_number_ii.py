class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(m, n):
            if m == 0:
                return ['']

            if m == 1:
                return ['0', '1', '8']

            prev = helper(m-2, n)
            cur = []
            for p in prev:
                if m != n:
                    cur.append('0' + p + '0')
                cur.append('1' + p + '1')
                cur.append('8' + p + '8')
                cur.append('6' + p + '9')
                cur.append('9' + p + '6')
            return cur

        return helper(n, n)