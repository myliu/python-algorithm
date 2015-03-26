class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        list1 = version1.split('.')
        list2 = version2.split('.')
        for i in range(max(len(list1), len(list2))):
            m = int(list1[i]) if i < len(list1) else 0
            n = int(list2[i]) if i < len(list2) else 0
            if m > n:
                return 1
            if m < n:
                return -1
        return 0


if __name__ == '__main__':
    s = Solution()
    print s.compareVersion('1.1.1', '1.2.0')