class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = version1.split('.')
        l2 = version2.split('.')
        m, n = len(l1), len(l2)
        for i in range(max(m, n)):
            v1 = int(l1[i]) if i < m else 0
            v2 = int(l2[i]) if i < n else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0


if __name__ == '__main__':
    s = Solution()
    print s.compareVersion('1.1.1', '1.2.0')